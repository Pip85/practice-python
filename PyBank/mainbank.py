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


num_months = len(months)
net_profit = sum(profit_loss)

print(months)
print(profit_loss)

# print(num_months)
# print(net_profit)

# Create new lists to hold months and profit/loss data without first row to calculate change in profit/loss
profit_loss2 = profit_loss[1:]
months2 = months[1:]

print(profit_loss2)
print(months2)

# zip months and profit/loss lists together to compare profit/loss
change=[]
zip_list = zip(profit_loss2, profit_loss)
for profit_loss2_i, profit_loss_i in zip_list:
    change.append(profit_loss2_i - profit_loss_i)

print(change)

# Calculate average change in profit/loss
avg_change = round(sum(change)/len(change),2)

print(avg_change)

# combined_change = zip(months2,profit_loss2)
# print(combined_change(-1))



# for key in combined_change:
#         k = key.split(",")
#         lst.append((k[0],k[1]))


# Pull data without first row into a dictionary
dictionary = dict(zip(months2, change))

print(dictionary)
print(dictionary.keys())


# Sort the profit/loss values in ascending order
import operator
plsort = sorted(dictionary.items(), key=operator.itemgetter(1))
sortdictionary={}
for item in plsort:
    for k in dictionary.keys():
        if dictionary[k] == item:
            sortdictionary[k] = dictionary[k]
            break

print(sortdictionary)


# print(plsort)
# dict1 = {1: 1, 2: 9, 3: 4}
# sorted_values = sorted(dict1.values()) # Sort the values
# sorted_dict = {}

# for i in sorted_values:
#     for k in dict1.keys():
#         if dict1[k] == i:
#             sorted_dict[k] = dict1[k]
#             break

# Calculate the greatest increase/decreases in profit/loss by month
# print(len((plsort).split(":")))


# greatinc = (plsort(key[-1]))
# print(greatinc)

# greatdec = plsort[0]
# print(greatdec)


# Create analysis of profit/loss
# print("Financial Analysis")
# print("-----------------------------------")
# print("Total Months:  $" + str(num_months))
# print("Average Change:  $" + str(avg_change))
# print("Greatest Increase in Profits:  " + str((greatinc).split(","))
