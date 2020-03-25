import pandas as pd


# Read from JHU Dataset
df = pd.read_csv("./COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")

# Remove Province/State, Latitude and Longitude columns
df = df.drop(columns=["Province/State", "Lat", "Long"])

# Add rows by Country/Region
df = df.groupby('Country/Region').sum()

# Output to CSV
df.to_csv("./output.csv")
