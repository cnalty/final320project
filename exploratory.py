import pandas as pd
import re
import pickle
import matplotlib.pyplot as plt


ranks = pd.read_csv("apranks.csv") # found here https://www.sports-reference.com/cbb/seasons/2019-polls.html

# The data is this table is formatted very poorly, so we're going to tidy, making date our rows and columns for each
# rank containing team name
print(ranks.head())



new_ranks = pd.DataFrame(index=[i for i in range(1, 26)])

# here we go through each data (and Final) add add the team names into each rank index with a new column for the date
for elem in ranks.columns:
    if re.match("(\d{1,2}\/\d{1,2})|(Final)", elem):
        date_dict = ranks.set_index("School")[elem].dropna().to_dict()
        rev_dict = {}
        for k, v in date_dict.items():
            rev_dict[v] = k

        new_ranks[elem] = pd.Series(rev_dict)

print(new_ranks.head())

# now we transpose the table to have the dates as the index as desired and add the year

new_ranks = new_ranks.transpose()

new_ranks = new_ranks.rename(index=lambda x: re.sub("^0.*", x + "/2019", x))
new_ranks = new_ranks.rename(index=lambda x: re.sub("^1.*", x + "/2018", x))

print(new_ranks.head())

# Now that we've cleaned the ranks data we can do some analysis on stats by rankings

serial_f = "dfs.dict"
dfs = pickle.load(open(serial_f, 'rb'))


# Ratio is assist turnover ratio
# APG is assists per game
# A is attempts not average
# PFPG is personal fouls per game
# Reb Marg is rebound margin
# SCR MAR scoring margin
# STPG steals per game
# useful stats TO / G, APG, BKPG, RPG, FG%, OPP FG%, FT%, PFPG, REB MARG, SCR MAR, STPG, 3PG, 3FG%

rank1s = new_ranks[1]

print(rank1s)


# Next lets graph some of the stats for rank #1 that are likely important to them winning
stats_to_graph = ["APG", "BKPG", "RPG", "FG%", "PFPG", "SCR MAR", "STPG", "3FG%"]
t_cols = {'Duke':'b', 'Gonzaga':'g', 'Kansas':'r', 'Tennessee':'m'}
for stat in stats_to_graph:
    for index in rank1s.index:
        if index in dfs.keys():
            curr_y = dfs[index].loc[dfs[index]['Name'] == rank1s[index]][stat].values[0]
            plt.scatter(index, curr_y, c=t_cols[rank1s[index]], label=rank1s[index])
            plt.annotate(rank1s[index], (index, curr_y))
    #plt.legend(t_cols.keys(), t_cols.values())
    plt.title(stat)

    plt.show()
