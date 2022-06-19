
# Bitcoin¶
# Consider a record of a one-time investment in bitcoin with value of that investment tracked monthly, provided as an (ordered) tuple of dictionaries, where each dictionary comprises one key for the month and corresponding one value for the value of the investment, and the first entry (Jan 2018) is the initial investment, like in data below.
#
# Write Python code to take such a record of any length, and output a table/dataframe comprising a row for each month with columns for date, start balance, and return. Print out this table/dataframe.
#
# Also, visualize the record as two vertically arranged plots.
#
# The top plot should show a line plot of start balance vs. month
# The bottom plot should show a bar plot of return vs. month, with a black horizontal line at return=0, and bars color-coded such that positive returns are green and negative returns are red.
# The two plots' horizontal axes should align. Demonstrate that your code works by applying it to data.
# Notes:
#
# The gain for each period is the end balance minus the start balance.
# The growth factor for each period is the end balance divided by the start balance.
import pandas as pd

data = ({"Jan 2018":1000},{"Feb 2018":1100},{"Mar 2018":1400},{"Apr 2018":700},{"May 2018":800},{"Jun 2018":500})

def return_on_investment(data):
    purchase = data[0]['Jan 2018']
    data = {k: [purchase, v, v - purchase] for d in data for k, v in d.items()}
    df = pd.DataFrame(data, index =['Purchase', 'Value', 'Gain'])
    return df.transpose()

print(return_on_investment(data))

df = return_on_investment(data)

ßß
