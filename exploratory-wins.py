import pandas as pd
import pickle
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#ranks = pd.read_csv("apranks.csv")

serial_f = "dfs.dict"
dfs = pickle.load(open(serial_f, 'rb'))

print(dfs['04/08/2019'].columns)

#stats_to_graph = ["APG", "BKPG", "RPG", "FG%", "PFPG", "SCR MAR", "STPG", "3FG%"]
#04 08 2019
#for stat in stats_to_graph:
#    plt.scatter(dfs['04/08/2019'][stat], dfs['04/08/2019'][])

    #for date in dfs.keys:
    #    for team in df['Name']:
    #        curr_y = dfs[date].loc[dfs[date]['Name']] == dfs[date]['Name'].values[0]
    #       plt.scatter(date, curr_y, c=t_cols[rank1s[index]])

#    plt.title(stat)
#    plt.legend(handles=patches)
#    plt.show()