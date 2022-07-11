# Import necessary libraries
import pandas as pd
from csv import reader
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import pandas_datareader.data as web
register_matplotlib_converters()

# Initialize variables
may_october = []
november_april = []
start_price = 0
begin = False
cur_date = None
begin = False

# Reads the csv file with the stock data from 1871
data = pd.read_csv('SandP_data.csv')

# For each row in the data sheet, get the necessary data and calculate the percent change
for i in range(len(data["Unnamed: 0"])):
    if str(data["Unnamed: 0"][i])[1].isnumeric():

        # Note, the years in the line below will be changed for each run through to keep the proper time frame
        if float(str(data["Unnamed: 0"][i])) > 2009 and float(str(data["Unnamed: 0"][i])) < 2022:

            # Store the current date
            if len(str(data["Unnamed: 0"][i])) == 7 and str(data["Unnamed: 0"][i])[1].isnumeric():
                cur_date = str(data["Unnamed: 0"][i])[5] + str(data["Unnamed: 0"][i])[6]

            # The number 10 was corrupted on the date sheet, so here is our accounting for that
            elif len(str(data["Unnamed: 0"][i])) == 6 and str(data["Unnamed: 0"][i])[1].isnumeric():
                cur_date = "10"
            else:
                cur_date = 0

            # Start on the first May of the data sheet so we have all complete time periods
            if cur_date == "05" and begin == False:
                begin = True

            # If it is May, begin time period
            if cur_date == "05" and data["Unnamed: 1"][1] is not None:
                start_price = data["Unnamed: 1"][i]

            # If it is October, finish time period at the end of the month
            if cur_date == "10" and data["Unnamed: 1"][1] is not None:
                may_october.append(((float(data["Unnamed: 1"][i]) - float(start_price)) / float(start_price)) * 100)

            # If it is the start of November, start next period
            if cur_date == "11" and data["Unnamed: 1"][1] is not None:
                start_price = data["Unnamed: 1"][i]

            # If it is the end of April, finish the time period
            if cur_date == "04" and data["Unnamed: 1"][1] is not None and begin == True:
                november_april.append(((float(data["Unnamed: 1"][i]) - float(start_price)) / float(start_price)) * 100)

# Remove any data that did not come through properly due to empty spaces in the data sheet
november_april = [x for x in november_april if str(x) != 'nan']
may_october = [x for x in may_october if str(x) != 'nan']

# Calculate the average of each list
may_october_avg = sum(may_october) / len(may_october)
november_april_avg = sum(november_april) / len(november_april)

# Create a figure and subplots
fig = plt.figure(figsize=(9, 7), dpi=200)
ax1 = fig.add_subplot(111)

# Graph the lines
lines = ax1.bar("May-October", may_october_avg, label='May-October')
lines = ax1.bar("November-April", november_april_avg, label='November-April')

# Get the title, axis labels, and formatting
ax1.set_title("S&P 500 May Effect 2009-2022 (Bull)", fontsize = 20, y = 1.02, weight = 'bold')
ax1.set_ylabel("Percent Change", fontsize = 15, weight = 'bold')
ax1.tick_params(labelsize=12);

# Save the figure
plt.savefig("May_Effect_2009_2022")
