# Importing libraries
import datetime
import pandas as pd
from csv import reader
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
import pandas_datareader.data as web
register_matplotlib_converters()

# Dictionary of presidents and their years served
president_dict = {"1877-1880":["R", "Hayes"], "1881-1884":["R", "Arthur"], "1885-1888":["D", "Cleveland 1st"], "1889-1892":["R", "Harrison"],
                    "1893-1896":["D", "Cleveland 2nd"], "1897-1900":["R", "McKinley"], "1901-1908":["R", "T Roosevelt"], "1909-1912":["R", "Taft"],
                    "1913-1920":["D", "Wilson"], "1921-1922":["R", "Harding"], "1923-1928":["R", "Coolidge"], "1929-1932":["R", "Hoover"],
                    "1933-1944":["D", "F Roosevelt"], "1945-1952":["D", "Truman"], "1953-1960":["R", "Eisenhower"], "1961-1962":["D", "J Kennedy"],
                    "1963-1968":["D", "Johnson"], "1969-1973":["R", "Nixon"], "1974-1976":["R", "Ford"], "1977-1980":["D", "Carter"],
                    "1981-1988":["R", "Reagan"], "1989-1992":["R", "G Bush"], "1993-2000":["D", "Clinton"], "2001-2008":["R", "G W Bush"],
                    "2009-2016":["D", "Obama"], "2017-2020":["R", "Trump"], "2021-2021":["D", "Biden"]}
president_list = []

# Import data from csv
data = pd.read_csv('SandP_data.csv')

# Define Variables
j = 0
starting_value = 0
closing_value = 0

# For each row in the datasheeet
for i in range(len(data["Unnamed: 0"])):

    # If the date is numeric (and not a label on the datasheet)
    if str(data["Unnamed: 0"][i])[1].isnumeric():

        # Assign the year and month to a variable
        year = int(str(data["Unnamed: 0"][i])[0:4])
        month = str(data["Unnamed: 0"][i])[5:]

        # If the year is the start of a new presidential term, save as the starting value
        if year == int(list(president_dict)[j][0:4]) and month == "01":
            starting_value = data["Unnamed: 1"][i]

        # If the year is the end of a presidential term, save as the ending value
        if year == int(list(president_dict)[j][5:]) and month == "12" or year == 2021 and month == "05":
            closing_value = data["Unnamed: 1"][i]

            # Calculate the percent change
            dif = ((float(closing_value) - float(starting_value)) / float(starting_value)) * 100

            # Add the results to the presidents percent change list
            president_list.append(dif)

            j += 1

# Define lists to be used on graph labels
names = []
colors = []

# For each president in the dictionary
for key in president_dict.keys():

    # Add their name to the list
    names.append(president_dict[key][1])

    # Add a color based off of the political party
    if president_dict[key][0] == "R":
        colors.append("r")
    else:
        colors.append("b")

# Define axis and data
fig, ax = plt.subplots(figsize=(14, 10), dpi=200)
bars = ax.barh(names, president_list, color = colors)

# Set title and axis labels
ax.set_title("Republican Vs Democrat", fontsize = 20, y = 1.02, weight = 'bold')
ax.set_xlabel("Percent Change Over Term", fontsize = 15, weight = 'bold')
ax.tick_params(labelsize=12);

# Add the percent change at the end of each bar
for bar in bars:
    width = round(bar.get_width(), 2) #Previously we got the height
    label_y_pos = bar.get_y() + bar.get_height() / 2
    if width > 0:
        ax.text(width + 1, label_y_pos, s=f'{width}', va='center')
    else:
        ax.text(width - 13, label_y_pos, s=f'{width}', va='center')

# Save the figure
plt.savefig("president_difference")
