from datetime import date
import calendar
from csv import reader
import calendar
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import pandas as pd

df = pd.DataFrame(columns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Year"])

list_of_symbols = ["SPY"]

for symbol in list_of_symbols:

    weekday_dict = {"Monday": [1], "Tuesday": [1], "Wednesday": [1], "Thursday": [1], "Friday": [1]}

    data = yf.download(symbol, start="1990-01-01", end="2021-01-01", interval = "1d")

    for i in range(len(data.index)):

        weekday = df.keys()[data.index[i].weekday()]

        pct_change = data["Close"][i] / data["Open"][i]

        weekday_dict[weekday].append(weekday_dict[weekday][len(weekday_dict[weekday]) - 1] * pct_change)

    for i in range(len(weekday_dict["Monday"])):
        df = df.append({"Monday" : weekday_dict["Monday"][i], "Tuesday": weekday_dict["Tuesday"][i], "Wednesday": weekday_dict["Wednesday"][i], "Thursday": weekday_dict["Thursday"][i], "Friday": weekday_dict["Friday"][i], "Year": data.index[i * 5]}, ignore_index = True)


    df.to_excel(f'data/{symbol}_cumlative.xlsx', index = False)
