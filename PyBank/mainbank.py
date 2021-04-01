# Run modules to import for op system and csv files
import os
import csv

# Store csv file path in variable
csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
profit_loss = []
# month_pl_d = {}

# Open/read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(csv_header)
    lines = csvfile.readlines()
    
    body = lines[0:]
         
#         # for line in csv.DictReader(csvreader):
#     #     print(line)

    for line in body:
        data = line.split(',')
        months.append(data[0])
        profit_loss.append(int(data[1]))

print(months)
print(profit_loss)

num_months = len(months)
net_profit = sum(profit_loss)

print(num_months)
print(net_profit)

profit_loss2 = profit_loss[1:]

print(profit_loss2)

change=[]
