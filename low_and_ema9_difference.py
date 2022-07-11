import datetime
from csv import reader
import calendar
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import xlwt
from xlwt import Workbook
import yfinance as yf
from pandas.plotting import register_matplotlib_converters
import datetime
register_matplotlib_converters()

close_price = []
sma20 = []
last_20 = []
difference_between = []
date = []
low_price = []
j = 0

wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('low_ema9_difference')

data = yf.download("^GSPC", start="1900-01-01", end="2021-01-01", interval = "1wk")

for row in data["Close"]:
    if row != "":
        close_price.append(float(row))

        if len(close_price) > 9:
            j = j + 1
            last_20.pop(0)
            last_20.append(float(row))
            total = 0
            print(len(last_20))
            for i in last_20:
                total += i
            sma20.append((total / 9))

        else:
            #sma20.append(0)
            last_20.append(float(row))


i = 0
for row in data["Low"]:
    i = i + 1
    if i > 9:
        if row != "":
            low_price.append(float(row))

for i in range(len(low_price) - 1):
    difference_between.append(((low_price[i] - sma20[i]) / low_price[i]) * 100)


sheet1.write(0, 0, "Date")
sheet1.write(0, 1, "Difference Between")
sheet1.write(0, 2, "Low Price")
sheet1.write(0, 3, "SMA 9")

for i in range(len(difference_between) - 1):

    sheet1.write(i + 1, 0, str(data.index[i]))
    sheet1.write(i + 1, 1, str(difference_between[i]) + "%")
    sheet1.write(i + 1, 2, low_price[i])
    sheet1.write(i + 1, 3, sma20[i])


fig = plt.figure(figsize=(12, 10), dpi=200)
ax1 = fig.add_subplot(111)
lines = ax1.plot(data.index[10:510], difference_between[:500], label='Close values')
ticks = ax1.get_xticks()
n = len(ticks) // 10  # Show 10 ticks.
ax1.grid()
plt.savefig("low_ema9_difference_shortened")
wb.save('low_ema9_difference_shortened.xls')
