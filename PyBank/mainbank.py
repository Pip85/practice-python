# Run modules to import for all op systems and csv files
import os
import csv

# Store csv file path in a variable
csvpath = os.path.join('Resources', 'budget_data.csv')

# Create lists to hold months and profit_loss information
months = []
profit_loss = []

# Open/read file & store header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(csv_header)

    lines = csvfile.readlines()
    
    # create variable to hold csv data without the header
    body = lines[0:]
   
   # Move months and profit_loss data into lists
    for line in body:
        data = line.split(',')
        months.append(data[0])
        profit_loss.append(int(data[1]))

# Determine the number of months in the period and net profit for the period from months and profit_loss lists
num_months = len(months)
net_profit = sum(profit_loss)

# Create new lists to hold data from months and profit_loss lists less the first row of data
profit_loss2 = profit_loss[1:]
months2 = months[1:]

# zip original profit_loss list with profit_loss2 list that excludes first row to calculate change in profit/loss by month
change=[]

zip_list = zip(profit_loss2, profit_loss)
for profit_loss2_i, profit_loss_i in zip_list:
    change.append(profit_loss2_i - profit_loss_i)

# Calculate average change in profit/loss
avg_change = round(sum(change)/len(change),2)

# Create dictionary to hold the months list less first row and the change in profit/loss by month
dictionary = dict(zip(months2, change))

# Create list and new dictionary to sort first dictionary by change values to determine greatest and least profit/loss change.
plsort={}
monthsort=[]

# Sort the profit/loss values in ascending order
import operator
plsort = sorted(dictionary.items(), key=operator.itemgetter(1))
print(plsort)

# import operator
# Holds sorted dictionary data
sorted_dict = {k: v for k, v in plsort}


profit_month = list(sorted_dict.keys())[-1]
profit = list(sorted_dict.values())[-1] 
loss_month = list(sorted_dict.keys())[0]
loss = list(sorted_dict.values())[0] 

# Create analysis of profit/loss to print to terminal
print("Financial Analysis")
print("-----------------------------------")
print("Total Months: " + str(num_months))
print("Total: $" + str(net_profit))
print("Average Change:  $" + str(avg_change))
print("Greatest Increase in Profits:  " + str(profit_month) + " ($" + str(profit) + ")")
print("Greatest Decrease in Profits:  " + str(loss_month) + " ($" + str(loss) + ")")

# Specify the file to write to
output_path = os.path.join("Analysis", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

# Initialize csv.writer
    txtwriter = csv.writer(txtfile)
    
# Print analysis to text file
    txtfile.writelines("Financial Analysis" + "\n")
    txtfile.writelines("---------------------------------------" + "\n")
    txtfile.writelines("Total Months: " + str(num_months) + "\n")
    txtfile.writelines("Total: $" + str(net_profit) + "\n")
    txtfile.writelines("Average Change:  $" + str(avg_change)+"\n")
    txtfile.writelines("Greatest Increase in Profits:  " + str(profit_month) + " ($" + str(profit) + ")" + "\n")
    txtfile.writelines("Greatest Decrease in Profits:  " + str(loss_month) + " ($" + str(loss) + ")")