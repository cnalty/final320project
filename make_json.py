import difflib
import json
import pandas as pd
import pickle

matches = {}
serial_f = "dfs.dict"
dfs = pickle.load(open(serial_f, 'rb'))
scores = pd.read_csv("box.csv")

for name in set(scores['win_team'].tolist()):
    if name not in dfs['04/08/2019']['Name'].tolist():
        closests = difflib.get_close_matches(name, dfs['04/08/2019']['Name'])
        if len(closests) == 0:
            print(name)
        else:
            matches[name] = closests

js = json.dumps(matches)
with open("matches", 'w+') as f:
    f.write(js)
