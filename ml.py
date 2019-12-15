import pandas as pd
import pickle
import json

serial_f = "dfs.dict"
dfs = pickle.load(open(serial_f, 'rb'))

serial_scores = "box.csv"

scores = pd.read_csv("box.csv")
print(scores.head())

#print(dfs.keys())

''' We choose to omit Scoring margin from '''

stats_to_use = stats_to_graph = ["BKPG", "FG%", "OPP FG%", "PFPG",
                                "STPG", "3FG%", "FT%", "REB MAR", "Ratio"]

with open("matches.json", 'r') as j:
    matches = json.load(j)

matches_rev = {}
for k, v in matches.items():
    matches_rev[v] = k

scores = scores.replace(matches_rev)
print(scores.head())
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



y = [val[2] for val in y_setup]
xs = []
total_missing = 0
wrong_names = set()
for result in y_setup:
    date = result[3]
    if date not in dfs.keys():
        continue
    if set(stats_to_use).issubset(set(dfs[date].columns)):
        print(dfs[date]["Name"].values)
        if result[0] not in dfs[date]["Name"].values:
            wrong_names.add(result[0])
        if result[1] not in dfs[date]["Name"].values:
            wrong_names.add(result[1])
        #team1_stats = [dfs[date][dfs[date]["Name"] == result[0]][stat] for stat in stats_to_use]
        #team2_stats = [dfs[date][dfs[date]["Name"] == result[1]][stat] for stat in stats_to_use]
        #team1_stats.extend(team2_stats)
        #xs.append(team1_stats)
    else:
        total_missing += 1

print(wrong_names)
print(len(wrong_names))
print("Oklahoma" in dfs["04/08/2019"]["Name"].values)
print(xs[0])

