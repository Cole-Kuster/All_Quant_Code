from datetime import date
import calendar
from csv import reader
import calendar
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import pandas as pd


list_of_symbols = list_of_symbols = ["SPY"]
year_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}

for symbol in list_of_symbols:

    df = pd.DataFrame(columns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Year"])
    df2 = pd.DataFrame(columns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Year"])

    data = yf.download(symbol, start="1993-01-01", end="2021-02-01", interval = "1d")

    prev_decade = str(data.index[0].year)[2]

    for i in range(len(data.index)):

        if str(data.index[i].year)[2] != str(prev_decade):
            avg = []

            for day in year_dict.keys():

                avg.append(sum(year_dict[day]) / len(year_dict[day]))


            df = df.append({"Monday" : avg[0], "Tuesday": avg[1], "Wednesday": avg[2], "Thursday": avg[3], "Friday": avg[4], "Year": prev_decade}, ignore_index = True)

            prev_decade = str(data.index[i].year)[2]
            year_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}

        weekday = df.keys()[data.index[i].weekday()]

        pct_change = ((data["Close"][i] - data["Open"][i]) / data["Open"][i]) * 100

        year_dict[weekday].append(pct_change)


    df.to_excel(f'data/{symbol}_weekday_by_decade.xlsx', index = False)

"""

    prev_decade = 7
    year_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    for i in range(len(df["Year"])):
        cur_decade = df["Year"][i][2]

        if cur_decade == prev_decade:
            for day in year_dict.keys():
                year_dict[day].append(df[day][i])

        else:
            avg = []
            prev_decade = cur_decade

            for day in year_dict.keys():
                avg =

"""
