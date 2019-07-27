import os
import csv
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

data = []
with open(budget_csv, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   for line in csvreader:
       data.append(line)

data.pop(0)
total = 0
for line in data:
   total += int(line[1])

total_diff = 0

for i in range(len(data)-1):
   curr_row = data[i]
   next_row = data[i+1]
   diff = int(next_row[1]) - int(curr_row[1])
   total_diff += diff
avg_diff = total_diff / (len(data)-1)   

#print(diff)
#print(total_diff)
#print(avg_diff)
#print(curr_row)
#print(next_row)
print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print("Total Months: ", len(data))
print("Total: ${:.2f}".format(total))
print("Average Change: ${:.2f}".format(avg_diff))

curr_max = int(data[1][1]) - int(data[0][1])
max_month = [0,1]
curr_min = int(data[1][1]) - int(data[0][1])
min_month = [0,1]

for i in range(len(data)-1):
    previous_month = data[i]
    next_month = data[i+1]
    previous_month_profitloss = int(previous_month[1])
    next_month_profitloss = int(next_month[1])
    diff = next_month_profitloss - previous_month_profitloss
    if diff > curr_max:
        curr_max = diff
        max_month = [i,i+1]    
    if diff > curr_max:
        curr_max = diff
        max_month = [i,i+1]
    if diff < curr_min:
        curr_min = diff
        min_month = [i,i+1]        
profit_month = [data[max_month[1]][0]]
loss_month = [data[min_month[1]][0]]
print("Greatest Increase in Profits:", profit_month, "${:.2f}".format(curr_max))
print("Greatest Decrease in Profits:", loss_month, "${:.2f}".format(curr_min))