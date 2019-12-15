import pandas as pd
import pickle


serial_f = "dfs.dict"
dfs = pickle.load(open(serial_f, 'rb'))

serial_scores = "box.csv"

scores = pd.read_csv("box.csv")
print(scores.head())

#print(dfs.keys())

''' We choose to omit Scoring margin from '''

stats_to_use = stats_to_graph = ["BKPG", "FG%", "OPP FG%", "PFPG",
                                "STPG", "3FG%", "FT%", "REB MAR", "Ratio"]


# First we need to randomize the data frame so we can randomly pick an even number of games where Team1 is the winner
# and where Team2 is the winner
scores = scores.sample(frac=1).reset_index(drop=True)

print(scores.head())
#team1, team2, winner, date

y_setup = []
cross_over = len(scores) / 2
for index, row in scores.iterrows():
    if index < cross_over:
        curr = (row['win_team'], row['lose_team'], 0, row['date'])
    else:
        curr = (row['lose_team'], row['win_team'], 1, row['date'])
    y_setup.append(curr)

# now we want to get the statistics we're going to be using for each team and line them up with the teams
import difflib
import json

matches = {}

for name in set(scores['win_team'].tolist()):
    if name not in dfs['04/08/2019']['Name'].tolist():
        closests = difflib.get_close_matches(name, dfs['04/08/2019']['Name'])
        if len(closests) == 0:
            print(name)
        else:
            matches[closests[0]] = name

js = json.dumps(matches)
with open("matches", 'w+') as f:
    f.write(js)


y = [val[2] for val in y_setup]
xs = []
for result in y_setup:
    date = result[3]
    if date not in dfs.keys():
        continue

    #team1_stats = [dfs[date].loc["Name" == result[0]][stat] for stat in stats_to_use]
    #team2_stats = [dfs[date].loc["Name" == result[1]][stat] for stat in stats_to_use]
    #team1_stats.extend(team2_stats)
    #xs.append(team1_stats)

#print(xs[0])
