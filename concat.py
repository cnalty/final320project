import pandas
import os
import io
import pickle

# the data dictionary
data = {}

# walk the files saved from the data download
for _, _, files in os.walk('data'):
    for file in files:
        csv = ""
        s = ""
        # open the file and create a new string with only the csv contents
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


for date in data.keys():
    # drop the rank column for each dataframe
    data[date] = data[date].drop("Rank", axis=1)

    # create win, win percent column and loss column
    WL = data[date]["W-L"].str.extract(r"(\d+)\-(\d+)")
    data[date]["Wins"] = WL[0].astype(float)
    data[date]["Losses"] = WL[1].astype(float)
    data[date]["Win%"] = data[date]["Wins"]/(data[date]["Losses"]+data[date]["Wins"])

    # drop columns that are unneeded
    data[date] = data[date].drop("W-L", axis=1)

    # change turn overs to be turn overs per game
    if "TO" in data[date]:
        data[date]["TO"] = data[date]["TO"].astype(float)/(data[date]["Wins"].astype(float)+data[date]["Losses"].astype(float))
        data[date] = data[date].rename({"TO": "TOPG"}, axis=1)

serial_f = "dfs.dict"

pickle.dump(data, open(serial_f, 'wb'))

''' To load the data, first we create a data dictionary. This will store multiple dataframes used to store team 
statistics for each date, using the date as the key in the dictionary. We then walk the directory with the dataframes 
in it, opening each of the near-4,000 CSV files. However, the CSV files are in an imperfect format, so certain lines 
must be ignored. We found that lines 1 - 10 and line numbers greater than 363 were not useful in each file. The useful
lines of the CSV file are stored in a string, which is parsed by pandas.read_csv to convert the CSV into a pandas 
dataframe. We then must determine if the date has been seen before, since many of the statistics and information are 
spread between multiple files. If it has been seen before, we add it to the dataframe corresponding to that date,
otherwise we add it to the dictionary as a new date. 

Then, we perform some data cleaning operations on the created dataframes. We choose to convert the W-L column, 
corresponding to the game wins to losses for a team at a given week, to 3 different columns. The first are the 
 game wins and losses, which are separated to assist later analysis, and then the win percent out of all games played
 by a team. We then convert the total turn overs for the season into a turn overs per game column. (This is the average
 of the turn overs for a team). '''
