import csv
import pandas as pd 

df = pd.read_csv("total_stars.csv")
for row in df:
    row.replace(","," ")
    

df.dropna()

del df["Luminosity"]
del df["Star_name1"]
del df["distance_from_earth1"]
del df["Mass"]
del df["Radius"]

df.to_csv("main.csv")