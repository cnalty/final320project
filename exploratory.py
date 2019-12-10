import pandas as pd
import re
import os

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




