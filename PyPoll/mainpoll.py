# Run modules to import for all op systems and csv files
import os
import csv

# # Build function to append csv file data to lists
# def list_read(list_data):
    

# Store csv file path in a variable
csvpath = os.path.join('Resources', 'election_data.csv')
# Create lists to hold months and profit_loss information

# Define variables to hold file attributes in lists
vote = []
candidate = []
list1 = []
count = []

column = 1

# Open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Store header in variable csv_header
    csv_header = next(csvreader)
    print(csv_header)

    # Create for loop to add each file column to a list
    for row in csvreader:
        vote.append(int(row[0]))
        candidate.append(row[2])
        list1.append(row[2])
        list1.append(int(row[0]))

print(len(candidate))

dictionary={}
for x, y in zip(candidate, vote):
    dictionary.setdefault(x, []).append(y)


cand_list = []

[cand_list.append(x) for x in candidate if x not in cand_list]

print(cand_list)

# i = cand_list[0]

# summary_list = count(x == i for x in dictionary.values())
# print(summary_list)



# # dictionary = dict(zip(candidate,vote))
# for key in candidate:
#     for value in vote:
#         dictionary[key] = value

# dictionary = {"candidate":"candidate", "vote_id":"vote"}

# dictionary = {key:value for key, value in zip(candidate, vote)}
# print(len(dictionary.keys()))
# print(dictionary.values())




# # dictionary = dict(zip(candidate, vote))


# vote_list = []
# [vote_list.append(x) for 

cand_votes=[]

cand_votes.append(candidate.count(str(cand_list[0])))
cand_votes.append(candidate.count(str(cand_list[1])))
cand_votes.append(candidate.count(str(cand_list[2])))
cand_votes.append(candidate.count(str(cand_list[3])))


print(cand_votes[0])
print(cand_votes[1])
print(cand_votes[2])
print(cand_votes[3])

dictionary2={}
for x, y in zip(cand_list, cand_votes):
    dictionary2.setdefault(x, []).append(y)

print(dictionary2.keys())
print(dictionary2.values())

for key,val in dictionary2.items():
    print(key, val)
    
all_votes=dictionary2.values()
max = max(all_votes)
print(max)

for candidate, vote in dictionary2.items():
    if vote==max:
        print(candidate)

# winner = dictionary2.index(str(max))
# print(winner)


# dictionary2.get(str(cand_list[0]))
# pair_list= []

# for pair in dictionary2.items():
#     pair_list.append(str((pair))
#     # print(str(pair.split(",")))

# print((str(pair_list[0]).split(","))



# print(str(dictionary2.keys[0]) + str(dictionary2.values[0])) 

# total_votes = (len(cand_votes))
# print(total_votes)

# max_votes = max(cand_votes)


# share=[]



# share.append(cand_votes[0]/total_votes)
# share.append(cand_votes[1]/total_votes)
# share.append(cand_votes[2]/total_votes)
# share.append(cand_votes[3]/total_votes)

# percent1 = round((share[0]),3)
# percent2 = round((share[1]),3)
# percent3 = round((share[2]),3)
# percent4 = round((share[3]),3)

# print("Election Results")
# print("-----------------------------------")
# print("Total Votes: " + str(total_votes))
# print("-----------------------------------")
# print(str(cand_list[0]) + ":   " + str(percent1) +"%   (" + str(cand_votes[0]) + ")")
# print(str(cand_list[1]) + ":   " + str(percent2) +"%   (" + str(cand_votes[1]) + ")")
# print(str(cand_list[2]) + ":   " + str(percent3) +"%   (" + str(cand_votes[2]) + ")")
# print(str(cand_list[3]) + ":   " + str(percent4) +"%   (" + str(cand_votes[3]) + ")")
# print("-----------------------------------")
# print("Winner:  " + 
# print("Average Change:  $" + str(avg_change))
# print("Greatest Increase in Profits:  " + str(res) + " ($" + str(res2) + ")")
# print("Greatest Decrease in Profits:  " + str(res3) + " ($" + str(res4) + ")")



# # print("Greatest Increase in Profits:  " + str((greatinc).split(","))
# # Specify the file to write to
# output_path = os.path.join("Analysis", "new.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as txtfile:

#     # Initialize csv.writer
#    # csvwriter = csv.writer(txtfile, delimiter=',')
#     txtwriter = csv.writer(txtfile)
#     # # Write the first row (column headers)
#     # csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

#     # Write the second row
#     # csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
    
      
#     line1 = ("Financial Analysis")
#     line2 = ("-----------------------------------")

#     txtfile.writelines("Financial Analysis" + "\n")
#     txtfile.writelines("---------------------------------------" + "\n")
#     txtfile.writelines("Total Months: " + str(num_months) + "\n")
#     txtfile.writelines("Total: $" + str(net_profit) + "\n")
#     txtfile.writelines("Average Change:  $" + str(avg_change)+"\n")
#     txtfile.writelines("Greatest Increase in Profits:  " + str(res) + " ($" + str(res2) + ")" + "\n")
#     txtfile.writelines("Greatest Decrease in Profits:  " + str(res3) + " ($" + str(res4) + ")")



# from collections import Counter


# Counter(candidate)
# print(Counter)

# # counter(candidate)
# print(counter)





# print(vote[0])
# print(county[0])
# print(candidate[0])
# print(len(candidate[0]))


# # Calculate total votes
# total_votes = len(vote)
# print(total_votes)
# print(len(candidate))



# voter_roll = dict(zip(candidate, vote))
# print(voter_roll)
# print(len(voter_roll))




# cand_list = []

# [cand_list.append(x) for x in candidate if x not in cand_list]

# print(cand_list)





# # print(dict([(key, len(values) for key, values in voter_roll.items()]))
# print(dict(voter_roll.keys(), len(voter_roll.values())))


# print(voter_roll.keys())
# print(len(voter_roll.keys()))

# counter = 0

# for key in voter_roll:
#     if voter_roll[key] == cand_list:
#         counter += 1

# print(dict([(key, sum(values)) for key, values in voter_roll.items()])
# # if key==cand.list:
#     print(voter_roll.keys())








# cand1 = []



# print(cand1)


# for x in voter_roll:
#     if voter_roll["name"][x] != cand_list[0]:





# print(cand1)

# # cand1=[]
# [cand1.append({voter_roll["name"][0]})

# # print(voter_roll[
# print(cand1[0])


# for x in voter_roll:
#     if cand_list[x] == voter_roll[name][x]:
#         cand1 = voter_roll[name][x], sum(voter_roll[name][x])
# print(cand1)



# first_vote = list(
# print([voter_roll

# cand_dict = {"candidate"
# # for x in candidate:
# #     if x not in cand_list:
# #         cand_list.append(candidate[x])

# # print(cand_list)



# Identify candidates and store in new list
# cand_list = []
# cand_list.append(candidate[0])
# print(cand_list)

# x = 1
# y = 0

# for x in candidate:
#     if candidate[x} != cand_list[y]:
#         cand_list.append(candidate[x])
#             if


# first_cand = candidate[0]
# print(first_cand)

# # Create list of candidate names

# if first_cand in candidate:


# print(candidate.index[0])
# print(candidate_sum)






# def read_csv(filename):
#     with open(csvpath) as csvfile:
#         file_data=csv.reader(csvfile)
#         headers=next(file_data)
#         return [dict(zip(headers,i)) for i in file_data]

# # print(dict.keys())
# csvfile = csv.DictReader(open(csvpath))
# # open the file if you want to iterate a second time.)

# for row in range(len(csvfile)):
#     print(row)





# csvreader = csv.reader(csvfile)
# # Open/read file & store header
# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')



#     lines = csvfile.readlines()
 

        
# with open(newfile.csv', 'w') as outfile:
#     writer = csv.writer(outfile)
#     mydict = {rows[0]:rows[1],rows[2] for rows in reader}   
# create variable to hold csv data without the header
#     body = lines[0:]
   
#    # Move months and profit_loss data into lists
#     for line in body:
#         data = line.split(',')
#         months.append(data[0])
#         profit_loss.append(int(data[1]))


# num_months = len(months)
# net_profit = sum(profit_loss)

# print(months)
# print(profit_loss)

# # Create new lists to hold months and profit/loss data without first row to calculate change in profit/loss
# profit_loss2 = profit_loss[1:]
# months2 = months[1:]

# print(profit_loss2)
# print(months2)

# # zip months and profit/loss lists together to compare profit/loss
# change=[]
# zip_list = zip(profit_loss2, profit_loss)
# for profit_loss2_i, profit_loss_i in zip_list:
#     change.append(profit_loss2_i - profit_loss_i)

# print(change)

# # Calculate average change in profit/loss
# avg_change = round(sum(change)/len(change),2)

# print(avg_change)

# # Pull data without first row into a dictionary
# dictionary = dict(zip(months2, change))

# print(dictionary)
# print(dictionary.keys())
# print(dictionary.values())

# plsort={}
# monthsort=[]
# # Sort the profit/loss values in ascending order
# import operator
# plsort = sorted(dictionary.items(), key=operator.itemgetter(1))
# print(plsort)

# import operator

# #dict1 = {1: 1, 2: 9, 3: 4}
# #sorted_tuples = sorted(dict1.items(), key=operator.itemgetter(1))
# #print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
# sorted_dict = {k: v for k, v in plsort}

# print(sorted_dict) # {1: 1, 3: 4, 2: 9}
# print(sorted_dict.keys())

# res = list(sorted_dict.keys())[-1]
# res2 = list(sorted_dict.values())[-1] 
# res3 = list(sorted_dict.keys())[0]
# res4 = list(sorted_dict.values())[0] 

# print("Financial Analysis")
# print("-----------------------------------")
# print("Total Months: " + str(num_months))
# print("Total: $" + str(net_profit))
# print("Average Change:  $" + str(avg_change))
# print("Greatest Increase in Profits:  " + str(res) + " ($" + str(res2) + ")")
# print("Greatest Decrease in Profits:  " + str(res3) + " ($" + str(res4) + ")")



# # print("Greatest Increase in Profits:  " + str((greatinc).split(","))
# # Specify the file to write to
# output_path = os.path.join("Analysis", "new.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as txtfile:

#     # Initialize csv.writer
#    # csvwriter = csv.writer(txtfile, delimiter=',')
#     txtwriter = csv.writer(txtfile)
#     # # Write the first row (column headers)
#     # csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

#     # Write the second row
#     # csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
    
      
#     line1 = ("Financial Analysis")
#     line2 = ("-----------------------------------")

#     txtfile.writelines("Financial Analysis" + "\n")
#     txtfile.writelines("---------------------------------------" + "\n")
#     txtfile.writelines("Total Months: " + str(num_months) + "\n")
#     txtfile.writelines("Total: $" + str(net_profit) + "\n")
#     txtfile.writelines("Average Change:  $" + str(avg_change)+"\n")
#     txtfile.writelines("Greatest Increase in Profits:  " + str(res) + " ($" + str(res2) + ")" + "\n")
#     txtfile.writelines("Greatest Decrease in Profits:  " + str(res3) + " ($" + str(res4) + ")")