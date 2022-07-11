from datetime import date
import calendar
from csv import reader
import calendar
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import pandas as pd


list_of_symbols = list_of_symbols = ["DIA", "DOW",  "IJH", "IWM", "QQQ", "SPY"]
year_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}

for symbol in list_of_symbols:

    df = pd.DataFrame(columns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Year"])
    df2 = pd.DataFrame(columns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Year"])

    data = yf.download(symbol, start="1993-01-01", end="2021-02-01", interval = "1d")

    prev_year = data.index[0].year

    for i in range(len(data.index)):

        if data.index[i].year > prev_year:
            avg = []

            for day in year_dict.keys():

                avg.append(sum(year_dict[day]) / len(year_dict[day]))


            df = df.append({"Monday" : avg[0], "Tuesday": avg[1], "Wednesday": avg[2], "Thursday": avg[3], "Friday": avg[4], "Year": prev_year}, ignore_index = True)

            prev_year = float(data.index[i].year)
            year_dict = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}

        weekday = df.keys()[data.index[i].weekday()]

        pct_change = ((data["Close"][i] - data["Open"][i]) / data["Open"][i]) * 100

        year_dict[weekday].append(pct_change)

    df.to_excel(f'data/{symbol}_weekday_by_year.xlsx', index = False)
