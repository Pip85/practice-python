# Run modules to import for all op systems and csv files
import os
import csv

# Create function to print dashed lines to terminal
def lines():
    print("----------------------------------")

# Create function to print dashed lines to text file
def lines_write():
    txtfile.writelines("---------------------------------------" + "\n")    

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

for index in range(len(cand_list)):
    cand_votes.append(candidate.count(cand_list[index]))

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
     
# Create list to hold the percentage of votes for each candidate
share_list=[]

for index in range(len(cand_votes)):
    share_list.append(cand_votes[index]/total_votes)
    
# Begin printing analysis to terminal
print("Election Results")
lines()
print(f'Total Votes: {total_votes}')
lines()

# Specify the file path to write analysis to text file
output_path = os.path.join("Analysis", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents.
with open(output_path, 'w', newline='') as txtfile:

# Initialize csv.writer
    txtwriter = csv.writer(txtfile)

# Output analysis to text file      
    txtfile.writelines("Election Results" + "\n")
    lines_write()
    txtfile.writelines(f'Total Votes: {total_votes} \n')
    lines_write()

# Create for loop to format the percentage data in share_list and print those results to the terminal and the text file
    for index, share in enumerate(share_list):
        percent = format((share*100),'.3f')
        candidate_name = (cand_list[index])
        candidate_vote = (cand_votes[index])
        print(f'{candidate_name} : {percent}% ({candidate_vote})')
        txtfile.writelines(f'{candidate_name} : {percent}% ({candidate_vote}) \n')

# Complete printing analysis to terminal
    lines()
    print("Winner:  " + winner)
    lines()

# Complete printing analysis to the text file    
    lines_write()
    txtfile.writelines("Winner:  " + winner + "\n")
    lines_write()
