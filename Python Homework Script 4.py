import os
import csv
election_csv = os.path.join("..", "Resources", "election_data.csv")

data = []
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for line in csvreader:
    	data.append(line)
 
data.pop(0)
total = 0
for line in data:
   total += 1