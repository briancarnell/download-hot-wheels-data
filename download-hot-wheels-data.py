import pandas as pd
import os

print("Enter the Hot Wheels model year you want to download:")
hot_wheels_year = input()
hot_wheels_url = "https://hotwheels.fandom.com/wiki/List_of_" + hot_wheels_year + "_Hot_Wheels"
df = pd.read_html(hot_wheels_url)
df = (df[0].astype(str))
df.to_csv("hot_wheels_" + hot_wheels_year +".csv", index=False)
