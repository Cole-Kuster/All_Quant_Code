# Import libraries
import datetime
import matplotlib.pyplot as plt
import yfinance as yf
from pandas.plotting import register_matplotlib_converters
import pandas as pd
register_matplotlib_converters()

# Create a list of the names and symbols we will be using
names_list = ["S&P 500 Index", "Gold", "Oil", "Oil Pre 2020"]
symbols_list = ["^GSPC", "XAU=F", "CL=F", "CL=F"]

# Loop through the list of names/symbols
for j in range(len(names_list)):

    # If the name is this specific one, change the end date to before 2020
    if names_list[j] == "Oil Pre 2020":
        data = yf.download(symbols_list[j], start="1993-01-01", end="2019-05-10", interval = "1d")
    # Otherwise, keep the end date in 2021
    else:
        data = yf.download(symbols_list[j], start="1995-01-01", end="2021-05-10", interval = "1d")

    # Create and empty this new list in each loop
    dif = []

    # Loop through the data for the given symbol
    for i in range(len(data["Open"])):
        # Make sure the data exists
        if data["Close"][i] != "" and data["Open"][i] != "":
            # Add the percent change from the day to the list
            dif.append(((data["Close"][i]/data["Open"][i]) - 1) * 100)


    # Create figure and axis
    fig = plt.figure(figsize=(8, 7), dpi=200)
    ax1 = fig.add_subplot(111)

    # Set a title and axis labels
    ax1.set_title(f"{names_list[j]} Daily Change", fontsize = 20, y = 1.02, weight = 'bold')
    ax1.set_xlabel("Year", fontsize = 15, weight = 'bold')
    ax1.set_ylabel("Daily Percent Change", fontsize = 15, weight = 'bold')
    ax1.tick_params(labelsize=12);
    ax1.grid()

    # Set the data
    lines = ax1.plot(data.index, dif, label='IntraDay')

    # Save the figure using the name list
    plt.savefig(f"{names_list[j]} Daily Extremes")
