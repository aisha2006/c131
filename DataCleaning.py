import csv
import pandas as pd

df = pd.read_csv("Brightstars.csv")
del df["luminosity"]
df.to_csv("newBrightstars.csv")

