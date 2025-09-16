# TIPPING BUCKET SCRIPT
# The objective of this script is to convert individual tip counts from a tipping bucket to daily precip totals.
# This script was written for Python pandas.

import pandas as pd

# Below are the two variables that the user must edit.
# Remember to add .csv at the end of your file names.

INPUT_FILE = 'Precip Data WC.csv'
OUTPUT_FILE = 'Precip_hourly.csv'

df = pd.read_csv(INPUT_FILE, skiprows=1)

# 'dt.floor('h')' groups the data by the hour while 'value_counts()' calculates how many rows there are in an hour
# which utimately gives us how many tips per hour using this dataset.

df = (pd.to_datetime(df['Date Time, GMT-07:00'])
        .dt.floor('h')
        .value_counts()
        .rename_axis('date')
        .reset_index(name='tip count')
        .sort_values('date'))

# Create a new column called 'precipitation (mm)'. Convert tip count to millimetre values. 1 tip = 0.2 mm.

df['precipitation (mm)'] = df['tip count']*0.2

df.to_csv(OUTPUT_FILE)