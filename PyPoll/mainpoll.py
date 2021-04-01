# Run modules to import for op system and csv files
import os
import csv

# Store csv file path in variable
csvpath = os.path.join('Resources', 'election_data.csv')

# Open/read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(csv_header)

    
#     # lines = csvfile.readlines()

# months = []
# profit_loss = []

# body = lines[1:]
# for line in body:
#     data = line.split(',')
#     months.append(data[0])
#     profit_loss.append(int(data[1]))

# num_months = len(months)
# net_profit = sum(profit_loss)
# beg_profit = int(profit_loss[0])
# end_profit = int(profit_loss[-1])


# print(profit_loss)
# print(months)
# print(len(months))
# print(net_profit)
# print(profit_loss[0])
# print(profit_loss[-1])



# #csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# csvpath = os.path.join('Resources', 'budget_data.csv')
# months = []
# profit_loss = []
# body = lines[1:]

# with open(csvpath) as csvfile:
#     # csvreader = csv.reader(csvfile, delimiter=',')
#     lines = csvfile.readlines()
#     csv_header = next(csvreader)

#     for row in csvreader:
#             month_pl[row[0]] = {'profit_loss':row[1]}

# print(month_pl)

# num_months = len(month_pl[0])

# print(num-months)



# for line in body:
#     data = line.split(',')
#     months.append(data[0])
#     profit_loss.append(int(data[1]))

# num_months = len(months)
# net_profit = sum(profit_loss)
# beg_profit = int(profit_loss[0])
# end_profit = int(profit_loss[-1])


# print(profit_loss)
# print(months)
# print(len(months))
# print(net_profit)
# print(profit_loss[0])
# print(profit_loss[-1])






# change = profit_loss[-1] - profit_loss[0]
# #average = change//((sum)profit_loss)

# print(change)
# #print(average)
# print(body)
# print(lines)

# def analysis(financials):
#     num_months = 




#________________________________________________________
# Unused Code
#________________________________________________________
# month_pl = {}
#for x in range(0, len(profit_loss)):
    #profit_loss[x] = int(profit_loss[x])
    #header = next(csvreader)
    #data = list(csvreader)
    #for row in data:
        #months.append(data[0])
        #profit_loss.append(data[1])

#print(profit_loss)
  
   #months = list(csvreader)
   #print(months)
    
   #for row in csvreader:
    #Total_Months = Total_Months + 1
    #Total = Total + (row[1])

#print (Total_Months)
#print (Total)

#print("Total Months = " + Total_Months)
#print("Total = " + Total)

#def analysis(Calculations):
 #   Total_Months = str(Calculations[0])
  #  Profits = float(Calculations[1])
   # Losses = float(Calcuations[2])

    #Total_Months = len(Total_Months)
    #Net = Profits - Losses

#with open('budget_data.csv', newline=' ') as csvfile:
 #   reader = csv.DictReader(csvfile,delimiter=',')

#Total_Months = 0
#Total = 0.0

#for row in csv_reader:
 #   Total_Months = Total_Months + 1
  #  Total = Total + float(row[1])

#print("Total Months = " + Total_Months)
#print("Total = " + Total)
