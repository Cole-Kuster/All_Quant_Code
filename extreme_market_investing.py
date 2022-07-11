# Import libraries
import matplotlib.pyplot as plt
import yfinance as yf
from pandas.plotting import register_matplotlib_converters
import datetime
import pandas as pd
register_matplotlib_converters()

# Create a list of the names and symbols we will be using
names_list = ["Bitcoin", "Dogecoin", "EURUSD", "Yen"]
symbols_list = ["Bitcoin.xls", "Doge_1.xls", "EURUSD2.xls", "Yen.xls"]

# Loop through the list of names/symbols
for j in range(len(symbols_list)):

    # Read in our data from an excel spreadsheet
    data = pd.read_excel(symbols_list[j], encoding='utf-16')

    # Create and empty this new list in each loop
    dif = []

    # Loop through the data for the given symbol
    for i in range(len(data["Open"])):
        # Make sure the data exists
        if data["Price"][i] != "" and data["Open"][i] != "":\
            # Add the percent change from the day to the list
            dif.append(((data["Price"][i]/data["Open"][i]) - 1) * 100)
            if dif[len(dif) - 1] > 300:
                print(data["Price"][i])
                print(data["Open"][i])
                print(data["Date"][i])


    # Create figure and axis
    fig = plt.figure(figsize=(8, 7), dpi=200)
    ax1 = fig.add_subplot(111)

    # Set a title and axis labels
    ax1.set_title(f"{names_list[j]} Daily Change", fontsize = 20, y = 1.02, weight = 'bold')
    ax1.set_xlabel("Year", fontsize = 15, weight = 'bold')
    ax1.set_ylabel("Daily Percent Change", fontsize = 15, weight = 'bold')
    ax1.grid()

    # Set the data
    lines = ax1.plot(data["Date"], dif, label='IntraDay')

    # Save the figure using the name list
    plt.savefig(f"{names_list[j]} Daily Extremes Alt Data")
