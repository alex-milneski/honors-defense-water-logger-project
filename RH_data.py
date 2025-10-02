import pandas as pd

# read csv skipping rows to make data columns readable
df = pd.read_csv('OCT_HOBO_tempRH.csv', skiprows=2)

# Renaming column to simplify the code.
df.rename({df.columns[1]: 'Date Time'}, axis=1, inplace=True)

# Converting to datetime format to make recognizing minutes possible.
df['Date Time'] = pd.to_datetime(df['Date Time'])

# dropping the rows that do not satisfy the condition '0 minutes' and
# resetting the index so that it does not skip every 2 lines
df = (df.loc[df['Date Time'].dt.minute == 0]
      .reset_index(drop=True)
      .drop('#', axis=1))


df.to_csv('RH_data_OCT.csv')