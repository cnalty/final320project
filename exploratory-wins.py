import pickle
import matplotlib.pyplot as plt


#ranks = pd.read_csv("apranks.csv")

serial_f = "dfs.dict"
dfs = pickle.load(open(serial_f, 'rb'))

stats_to_graph = ["TOPG", "APG", "BKPG", "RPG", "FG%", "OPP FG%", "PFPG",
                  "SCR MAR", "STPG", "3FG%", "FT%", "REB MAR", "3PG", "Ratio"]
stats_to_name = {"TOPG" : "Turn Overs Per Game",
                 "APG" : "Assists Per Game",
                 "BKPG" : "Blocks Per Game",
                 "RPG" : "Rebounds Per Game",
                 "FG%" : "Field Goal Percent",
                 "OPP FG%" : "Opposition Field Goal Percent",
                 "PFPG" : "Personal Fouls Per Game",
                 "SCR MAR" : "Score Margin",
                 "STPG" : "Steals Per Game",
                 "3FG%" : "3-Point Field Goal Percent",
                 "FT%" : "Free Throw Percent",
                 "REB MAR" : "Rebound Margin",
                 "3PG" : "3-Points Per Game",
                 "Ratio" : "Assist to Turnover Ratio"}
# iterate the stats and make a plot for each one
for stat in stats_to_graph:
    # get the values for the end of season data, dropping NAN values
    plt.scatter(dfs['04/08/2019'][stat].dropna(), dfs['04/08/2019']["Win%"].dropna())

    # set the graph labels
    plt.xlabel(stats_to_name[stat])
    plt.ylabel("Win Percent")
    plt.title(stats_to_name[stat] + " vs Win Percent")

    plt.show()

''' We now create multiple scatter plots of a statistic on the x axis, and the win percentages of all the teams on the 
y axis. We do this by creating a list of statistics we want to plot against win percentage, and then using matplotlib
we create multiple plots, each with a unique name. We use dropna() to remove any missing values. Since we only want to 
view the general trends in the data, it is not important to keep every value to plot the data. We will use the scatter 
plots to determine which statistics are the best to predict a win for any college basketball team, given certain inputs.
 
From the graphs, it is clear that certain statistics will provide insight to which teams are going to win a game. Some
statistics, like score margin (the average amount a team wins a game over the opponent), present a near perfect relation
to win percentage. However, this cannot be used in the regression model since it is a data leakage problem (meaning the 
prediction data implicitly contains the result). This means our predictions would be putting too much value in the 
results for the score margin. You can read more about data leakage at this link from Towards Data Science. 
https://towardsdatascience.com/data-leakage-in-machine-learning-10bdd3eec742. 

Other statistics do not pose such a problem and still show a general trend following the win percentage. Some of these
statistics show a negative trend, meaning that the higher the statistic, the more likely it is a team will lose, and 
others show a positive trend, meaning the higher the statistic the more likely a team is to win. Positive trends are 
seen in the rebound margin, free throws per game, 3-Point field goal percent, steals per game, assists per game , and 
blocks per game statistics, while negative trends are shown in the turn overs per games and opposition field goal 
percent. Some data shows little correlation to the win percent, such as the personal fouls per game and rebounds per 
game. The statistics with trends will be used later in the predictive regression model. '''