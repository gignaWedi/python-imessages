import os
import pandas as pd
import toml

data = toml.load("config.toml")

def send(buddy, message):
	os.system(f'osascript sendMessage.applescript "{buddy}" "{message}"')

sheet = f'https://docs.google.com/spreadsheets/d/{data["sheet_id"]}/export?format=csv&sheet={data["sheet_name"]}'

df = pd.read_csv(sheet)


# Edit Code after this line

df.apply(lambda row: send(row["Number"], row["Message"]), axis = 1)

