import csv

data = []

with open("Brightstars.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

headers = data[0]
starData = data[1:]
starRadius = []
starMass = []

for i in starData:
  i[4]=float(i[4])*0.102763
  starRadius.append(i[4])
for i in starData:
  i[3]=float(i[3])*0.000954588
  starMass.append(i[3])

