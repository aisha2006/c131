from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(START_URL)

soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find_all("table")
temp_list = []
table_rows = star_table[7].find_all("tr")
for i in table_rows:
    td = i.find_all("td")
    row = [j.text.rstrip() for j in td]
    temp_list.append(row)

star_names = []
mass = []
distance = []
radius = []
lum = []

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    lum.append(temp_list[i][7])
    radius.append(temp_list[i][6])

df = pd.DataFrame(list(zip(star_names, distance, mass, radius, lum)), columns = ["star_name", "distance", "mass", "radius", "luminosity"])
df.to_csv("Brightstars.csv")

df = df[df['distance'].notna()]
df = df[df['mass'].notna()]
df = df[df['radius'].notna()]
df = df[df['luminosity'].notna()]

# df[df['mass']] = float(df[df['mass']])*0.000954588
# df[df['radius']] = float(df[df['radius']])*0.102763

temp_star_list = []
