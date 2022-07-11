# Import libraries
import datetime
import matplotlib
import matplotlib.pyplot as plt
import yfinance as yf
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Initialize lists to be used later
years = []
close_price = []
open_price = []
dif_intra = []
dif_overnight = []

# Download daily data for a given symbol
data = yf.download("IJH", start="1993-01-01", end="2021-05-10", interval = "1d")

# Create a list for the close price
for row in data["Close"]:
    if row != "":
        close_price.append(float(row))

# Create a list for the open price
for row in data["Open"]:
    if row != "":
        open_price.append(float(row))

# Calculate the intraday and overnight difference for each day on the list
for i in range(len(close_price) - 1):
    dif_intra.append(close_price[i + 1] / open_price[i + 1])
    dif_overnight.append(open_price[i + 1] / close_price[i])

# Give variables starting values
dif_intra_total = 1
dif_intra_list = []
# Loop the each item in the intraday list
for item in dif_intra:
    # Multiply the current value to the previos value
    dif_intra_total = dif_intra_total * item
    # Add this to the new intraday list
    dif_intra_list.append(dif_intra_total)

# Loop the each item in the overnight list
dif_overnight_total = 1
dif_overnight_list = []
# Loop the each item in the overnight list
for item in dif_overnight:
    # Multiply the current value to the previos value
    dif_overnight_total = dif_overnight_total * item
    # Add this to the new overnight list
    dif_overnight_list.append(dif_overnight_total)

# Create the figure and axis
fig = plt.figure(figsize=(8, 7), dpi=200)
ax1 = fig.add_subplot(111)
ax2 = fig.add_subplot(111)

# Set title and axis labels
ax1.set_title("IJH Overnight vs Intraday", fontsize = 20, y = 1.02, weight = 'bold')
ax1.set_xlabel("Year", fontsize = 15, weight = 'bold')
ax1.set_ylabel("Factor Increased By", fontsize = 15, weight = 'bold')
ax1.legend()
ax2.legend()
ax1.tick_params(labelsize=12);
ax1.grid()

# Set the data
lines = ax1.plot(data.index[1:], dif_intra_list, label='IntraDay')
lines = ax2.plot(data.index[1:], dif_overnight_list, label='Overnight')

# Save the figure
plt.savefig("IJH Overnight Gap FINAL")
