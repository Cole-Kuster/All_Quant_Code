import datetime
from csv import reader
import calendar
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import xlwt
from xlwt import Workbook

close_price = []
sma20 = []
last_20 = []
difference_between = []
date = []
j = 0   

wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('PriceData(2_Month)')

with open("S&P 1871 All Data.csv", 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        if row[7] != "" and not row[7].isalpha():
            close_price.append(float(row[7]))
            date.append(row[0])

            if len(close_price) > 2:
                j = j + 1
                last_20.pop(0)
                last_20.append(float(row[7]))
                total = 0
                for i in last_20:
                    total += i
                sma20.append((total / 2))

                print(str(date[len(date) - 1]) + " close price: " + str(close_price[len(close_price) - 1]) + " sma5: " + str(sma20[len(sma20) - 1]))
                sheet1.write(j, 0, str(date[len(date) - 1]))
                sheet1.write(j, 1, str(close_price[len(close_price) - 1]))
                sheet1.write(j, 2, str(sma20[len(sma20) - 1]))


                difference_between.append(close_price[len(close_price) - 1] - sma20[len(sma20) - 1])
            else:
                sma20.append(0)
                last_20.append(float(row[7]))











#mydict = pd.read_csv('SPY_Weekly.csv', header=None, index_col=0, squeeze=True).to_dict()

# Plot the close price of the AAPL

#plot = plt.plot(date, close_price)
#plt.plot(sma20)

##for label in plot.ax.xaxis.get_ticklabels()[::2]:
#    label.set_visible(False)

fig = plt.figure(figsize=(12, 10), dpi=200)
ax1 = fig.add_subplot(111)
lines = ax1.plot(date, close_price, label='Close values')
ax2 = fig.add_subplot(111)
lines = ax1.plot(sma20, label='SMA20 values')
ticks = ax1.get_xticks()
n = len(ticks) // 10  # Show 10 ticks.
ax1.set_xticks(ticks[::n])
ax1.set_xticklabels(date[::n])
ax1.grid()


wb.save('PriceData(2_month).xls')
#plt.figure(figsize=(10, 10))
plt.savefig("YYYY 2 month")
