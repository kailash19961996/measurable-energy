import pandas as pd

# Load the data (semicolon-separated, with some missing values)
df = pd.read_csv('household_power_consumption.txt', sep=';', 
                 parse_dates={'datetime': ['Date', 'Time']}, 
                 infer_datetime_format=True, 
                 na_values='?', 
                 low_memory=False)

# Focus on Global_active_power (in kilowatts) and resample to hourly data
df = df.set_index('datetime')
df = df['Global_active_power'].resample('H').mean().fillna(method='ffill')

# Take a smaller subset (e.g., 1 month) for simplicity
df = df['2007-01-01':'2007-01-31']

# Save to a lightweight CSV
df.to_csv('energy_data.csv')
print("Preprocessed data saved to energy_data.csv")