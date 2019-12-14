import pandas
import os
import io
import re
import pickle

# the data dictionary
data = {}

# walk the files saved from the data download
for _, _, files in os.walk('data'):
    for file in files:
        csv = ""
        s = ""
        # open the file and create a new string with only the csv contents
        print(file)
        with open(os.path.join("data/", file), 'r') as f:
            s = f.read()
            i = 0
            date = ""
            for line in s.splitlines():
                if i == 8:
                    date = line[14:]
                # every file is identical, so these are the known lines which will contribute to the data
                if (i > 10 and i < 363 or i == 364 or i == 365) and "," in line:
                    csv += line+"\n"
                    if len(line) > 85:
                        print(line)
                i = i + 1
        # read the csv string and add to the dictionary if the data doesn't exist, or add to a dataframe in the
        # dictionary if it does exist
        if date in data:
            ndata = pandas.read_csv(io.StringIO(csv))
            for c1 in data[date].columns:
                if c1 in ndata.columns and c1 != "Name":
                    del ndata[c1]
            data[date] = data[date].merge(ndata)
        else:
            data[date] = pandas.read_csv(io.StringIO(csv))

if not os.path.isdir("dfs"):
    os.mkdir("dfs")

for date in data.keys():
    # drop the rank column for each dataframe
    data[date] = data[date].drop("Rank", axis=1)

    # create win, win percent column and loss column
    data[date] = data[date].append(data[date]["W-L"].str.extract(r"(\d+)-(\d+)"))
    data[date]["Wins"] = data[date][0].astype(float)
    data[date]["Losses"] = data[date][1].astype(float)
    data[date]["Win%"] = data[date]["Wins"]/data[date]["Losses"]

    # drop columns that are unneeded
    data[date] = data[date].drop(1, axis=1)
    data[date] = data[date].drop(0, axis=1)
    data[date] = data[date].drop("W-L", axis=1)

serial_f = "dfs.dict"

pickle.dump(data, open(serial_f, 'wb'))


