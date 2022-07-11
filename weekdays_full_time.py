# Import Libraries
from datetime import date
import yfinance as yf
import pandas as pd

# Create our dictionary and dataframe
year_dict1 = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Year": []}
days_pct = pd.DataFrame(columns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Monday","Year"])

# The list of symbols we will use with Yahoo Finance
#list_of_symbols = ["SPY", "QQQ", "DIA", "IJH", "IJK", "IWM"]
#list_of_symbols = ["VBR", "SCHA", "VBK", "IWO"]
list_of_symbols = ["^IXIC"]

# Loop through the symbols
for symbol in list_of_symbols:

    # Gather data
    data = yf.download(symbol, start="1900-01-01", end="2021-07-23", interval = "1d")

    # Loop through data
    for i in range(len(data.index)):

        # Find the weekday
        weekday = days_pct.keys()[data.index[i].weekday()]

        # Calculate the percentage
        pct_change = ((data["Close"][i] - data["Open"][i]) / data["Open"][i]) * 100

        # Append the percrnt change to the weekday
        year_dict1[weekday].append(pct_change)

        # Once a week we add the date for the week
        if weekday == "Monday":
            year_dict1["Year"].append(data.index[i])

    # Loop through the dictionary and add it to the dataframe
    # We do it this way so that there are no empty rows in the dataframe
    for i in range(len(year_dict1["Monday"])):
        days_pct = days_pct.append({"Monday" : year_dict1["Monday"][i], "Tuesday": year_dict1["Tuesday"][i], "Wednesday": year_dict1["Wednesday"][i], "Thursday": year_dict1["Thursday"][i], "Friday": year_dict1["Friday"][i], "Year" : year_dict1["Year"][i]}, ignore_index = True)

    # Save the data
    days_pct.to_excel(f'data/{symbol}_weekday_full_time.xlsx', index = False)

    # Reset the dictionary and dataframe for the next symbol
    year_dict1 = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Year": []}
    days_pct = pd.DataFrame(columns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Monday","Year"])
