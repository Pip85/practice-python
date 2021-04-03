# Run modules to import for all op systems and csv files
import os
import csv

# Store csv file path in a variable
csvpath = os.path.join('Resources', 'election_data.csv')

# Define variables to hold file attributes in lists; vote will hold voter ID, candidate will hold candidate name
vote = []
candidate = []

# Open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Store header in variable csv_header
    csv_header = next(csvreader)
    print(csv_header)

# Create for loop to addd the candidate name and voter ID data to the candidate and vote lists
    for row in csvreader:
        vote.append(int(row[0]))
        candidate.append(row[2])

# Determine total count of votes        
total_votes = (len(candidate))

# Create list to hold one instance of each candidate's name; append candidates from the candidates list to the cand_list if they are not already in cand_list
cand_list = []
[cand_list.append(x) for x in candidate if x not in cand_list]

# Determine total number of candidates
cand_num = len(cand_list)

# Determine votes for each of the candidates in cand_list and put them in cand_votes.
cand_votes=[]

cand_votes.append(candidate.count(str(cand_list[0])))
cand_votes.append(candidate.count(str(cand_list[1])))
cand_votes.append(candidate.count(str(cand_list[2])))
cand_votes.append(candidate.count(str(cand_list[3])))

# Create second dictionary to hold the total votes by candidate
cand_total={}
for x, y in zip(cand_list, cand_votes):
    cand_total.setdefault(x, []).append(y)

# Hold all cand_total dictionary values in one variable and determine the max value  
all_votes=cand_total.values()
max_vote = max(all_votes)

# Determine the winner of the election
for candidate, vote in cand_total.items():
    if vote==max_vote:
       winner = candidate
       print(winner)

# Create list to hold the percentage of votes for each candidate
share=[]

share.append(cand_votes[0]/total_votes)
share.append(cand_votes[1]/total_votes)
share.append(cand_votes[2]/total_votes)
share.append(cand_votes[3]/total_votes)

# Format share list contents as percentages with 3 decimal places
percent0 = format((share[0]*100),'.3f')
percent1 = format((share[1]*100),'.3f')
percent2 = format((share[2]*100),'.3f')
percent3 = format((share[3]*100),'.3f')

# Print results to terminal
print("Election Results")
print("-----------------------------------")
print(f'Total Votes: {total_votes}')
print("-----------------------------------")
print(f'{cand_list[0]} : {percent0}% ({cand_votes[0]})')
print(f'{cand_list[1]} : {percent1}% ({cand_votes[1]})')
print(f'{cand_list[2]} : {percent2}% ({cand_votes[2]})')
print(f'{cand_list[3]} : {percent3}% ({cand_votes[3]})')
print("-----------------------------------")
print("Winner:  " + winner)
print("-----------------------------------")

# Specify the file to write to
output_path = os.path.join("Analysis", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents.
with open(output_path, 'w', newline='') as txtfile:

# Initialize csv.writer
    txtwriter = csv.writer(txtfile)

# Output analysis to text file      
    txtfile.writelines("Election Results" + "\n")
    txtfile.writelines("---------------------------------------" + "\n")
    txtfile.writelines(f'Total Votes: {total_votes} \n')
    txtfile.writelines("-----------------------------------" + "\n")
    txtfile.writelines(f'{cand_list[0]} : {percent0}% ({cand_votes[0]}) \n')
    txtfile.writelines(f'{cand_list[1]} : {percent1}% ({cand_votes[1]}) \n')
    txtfile.writelines(f'{cand_list[2]} : {percent2}% ({cand_votes[2]}) \n')
    txtfile.writelines(f'{cand_list[3]} : {percent3}% ({cand_votes[3]}) \n')
    txtfile.writelines("-----------------------------------" + "\n")
    txtfile.writelines("Winner:  " + winner + "\n")
    txtfile.writelines("-----------------------------------")
