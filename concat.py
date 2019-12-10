import pandas
import os
import io
import re

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
                if (i > 10 and i < 363 or i == 364 or i == 365) and "," in line:
                    csv += line+"\n"
                    if len(line) > 85:
                        print(line)
                i = i + 1
        if date in data:
            ndata = pandas.read_csv(io.StringIO(csv))
            for c1 in data[date].columns:
                if c1 in ndata.columns and c1 != "Name":
                    del ndata[c1]
            data[date] = data[date].merge(ndata)
        else:
            data[date] = pandas.read_csv(io.StringIO(csv))
df = pandas.DataFrame(pandas.np.empty((0, 2)))
df.columns = ['Date', 'Data']

if not os.path.isdir("dfs"):
    os.mkdir("dfs")

for k in data.keys():
    data[k] = data[k].drop("Rank", axis=1)
    dash_date = re.sub(r"/", "-", k)
    data[k].to_csv(os.path.join("dfs/", dash_date + ".csv"))
df.to_csv("data.csv")


