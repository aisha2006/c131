import csv
import pandas as pd

df = pd.read_csv("newBrightstars.csv")
rows = []
with open("newBrightstars.csv", "r") as f:
  reader = csv.reader(f)
  for i in reader:
    rows.append(i)

headers = rows[0]
planet_data_rows = rows[1:]
temp_planet_data_rows = list(planet_data_rows)
for i in temp_planet_data_rows:
  planet_mass = i[5]
  if planet_mass.lower()=="unknown":
    planet_data_rows.remove(i)
    continue
  else:
    planet_mass_value = planet_mass.split(" ")[0]
    planet_mass_value = float(planet_mass_value)*1.989e+30
    i[3] = planet_mass_value
  
  planet_radius = i[6]
  if planet_radius.lower()=="unknown":
    planet_data_rows.remove(i)
    continue
  else:
    planet_radius_value = planet_radius.split(" ")[0]
    planet_radius_value = float(planet_radius_value)*6.957e+8
    i[6] = planet_radius_value

temp_planet_data_rows = list(planet_data_rows)
   
planet_masses = []
planet_radii = []
planet_names = []

for i in planet_data_rows:
  planet_masses.append(i[5])
  planet_radii.append(i[6])
  planet_names.append(i[3])

planet_gravity = []
for i,name in enumerate(planet_names):
  gravity = (float(planet_masses[i])*5.972e+24)/(float(planet_radii[i])*float(planet_radii[i])*6371000*6371000)*6.674e-11
  planet_gravity.append(gravity)

with open("newBrightstars.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerow(gravity)
    writer.writerows(planet_data_rows)
