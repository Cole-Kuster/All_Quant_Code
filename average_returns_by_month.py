import datetime
import calendar
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import pandas as pd

list_of_symbols = ["SPY"]
#"DIA", "DOW", "IJH", "IWM", "QQQ", "SPY"
month_index = {"1": "Jan", "2" : "Feb", "3" : "Mar", "4": "Apr", "5" : "May", "6" : "Jun", "7": "Jul", "8" : "Aug", "9" : "Sep", "10": "Oct", "11" : "Nov", "12" : "Dec"}
for symbol in list_of_symbols:
    data_dict = {"Jan" : [], "Feb" : [], "Mar" : [], "Apr" : [], "May" : [], "Jun" : [], "Jul" : [], "Aug" : [], "Sep" : [], "Oct" : [], "Nov" : [], "Dec" : []}

    data = yf.download(symbol, start = "1970-01-01", end = "2021-08-30", interval = "1mo")

    for i in range(len(data["Close"]) - 1):

        pct_change = ((data["Close"][i] / data["Open"][i]) - 1) * 100

        if str(data.index[i])[8] == "0" and str(data.index[i])[9] == "1":
            month = month_index[str(data.index.month[i])]
            data_dict[month].append(pct_change)

    new_data_dict = {}
    for key in data_dict.keys():

        avg = (sum(data_dict[key]) / len(data_dict[key]))
        new_data_dict[key] = avg

    plt.bar(new_data_dict.keys(), new_data_dict.values())
    plt.title("" + symbol + " Monthly Data")
    plt.xlabel("Month")
    plt.ylabel("Average % Change")
    plt.savefig('monthly_' + symbol + '.png', dpi=200)
