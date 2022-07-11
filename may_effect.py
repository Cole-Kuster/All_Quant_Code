# Import necessary libraries
import xlwt
from xlwt import Workbook
import pandas as pd
from csv import reader
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import pandas_datareader.data as web
import yfinance as yf
register_matplotlib_converters()

# Start a xls workbook to save the data in a spreadhseet
wb = Workbook()
sheet1 = wb.add_sheet('May_Effect')

# Initialize variables
may_september = []
november_april = []
start_price = 0
begin = False

# Download the data from yahoo finance using the yfinance api
# Note, the symbol must be changed with each run through
data = yf.download("SPY", start="1900-01-01", end="2021-05-01", interval = "1mo")

# Loop through the data
for i in range(len(data.index)):

    # Begin on the first May of the data set
    if int(data.index[i].month) == 5 and begin == False:
        begin = True

    if begin:

        # If it is May, start the time period
        if int(data.index[i].month) == 5:
            start_price = data["Open"][i]

        # Finish time period at the end of October
        elif int(data.index[i].month) == 10:
            may_september.append(((data["Close"][i] - start_price) / start_price) * 100)

        # Start next time period at the beginning of November
        elif int(data.index[i].month) == 11:
            start_price = data["Open"][i]

        # Finish time period at the end of April
        elif int(data.index[i].month) == 4:
            november_april.append(((data["Close"][i] - start_price) / start_price) * 100)

# Remove any incomplete data fromt the lists
november_april = [x for x in november_april if str(x) != 'nan']
may_september = [x for x in may_september if str(x) != 'nan']

# Get the average for each list
may_september_avg = sum(may_september) / len(may_september)
november_april_avg = sum(november_april) / len(november_april)

# Create a figure and subplots
fig = plt.figure(figsize=(8, 7), dpi=200)
ax1 = fig.add_subplot(111)

# Graph the lines
lines = ax1.bar("May-October", may_september_avg, label='May-September')
lines = ax1.bar("November-April", november_april_avg, label='November-April')

# Get the title, axis labels, and formatting
ax1.set_title("SPY May Effect", fontsize = 20, y = 1.02, weight = 'bold')
ax1.set_ylabel("Percent Change", fontsize = 15, weight = 'bold')
ax1.tick_params(labelsize=12);

# Save the figure
plt.savefig("SPY_May_Effect_FINAL")
wb.save('SPY_May_Effect_FINAL.xls')
