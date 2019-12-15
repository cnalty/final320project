import pandas as pd
import pickle

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

serial_f = "dfs.dict"
dfs = pickle.load(open(serial_f, 'rb'))

serial_scores = "box.csv"

scores = pd.read_csv("box.csv")

''' We choose to omit Scoring margin from '''

stats_to_use = stats_to_graph = ["BKPG", "FG%", "OPP FG%", "PFPG",
                                "STPG", "3FG%", "FT%", "REB MAR", "Ratio"]


