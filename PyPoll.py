# Import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('election_data.csv')
print("Election Results")
print("__________________")
votes = []
candidates = []


# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter = ',')
    # Read the header row first (skip this step if there is no header)
   print(csvreader)
   csv_header = next(csvreader)
   print(f"CSV Header: {csv_header}")
    # Read the header row first (skip this step if there is no header)

   for column in csvreader:
       votes.append(column[0])
       candidates.append(column[2])

   Total_Votes = (len(votes))
   print(f"Total Votes: {Total_Votes}")
   #Count each number of candidates in the candidates list
   Khan = int(candidates.count("Khan"))
   Correy = int(candidates.count("Correy"))
   Li = int(candidates.count("Li"))
   O_Tooley = int(candidates.count("O'Tooley"))
   #Get a percentage of each candidates vote total
   Khan_percentage = (Khan/Total_Votes) * 100
   Correy_percentage = (Correy/Total_Votes) * 100
   Li_percentage = (Li/Total_Votes) * 100
   O_Tooley_percentage = (O_Tooley/Total_Votes) * 100
   #Print each candidate's name, vote percentage, and raw number of votes
   print(f"Khan: {Khan_percentage}% ({Khan})")
   print(f"Correy: {Correy_percentage}% ({Correy})")
   print(f"Li: {Li_percentage}% ({Li})")
   print(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley})")
    #Compare Votes and pick winner with the most votes
   if Khan > Correy > Li > O_Tooley:
       Winner = "Khan"
   elif Correy > Khan > Li > O_Tooley:
       Winner = "Correy"
   elif Li > Khan > Correy > O_Tooley:
       Winner = "Li"
   elif O_Tooley > Khan > Correy > Li:
       Winner = "O'Tooley"
   print(f"Winner: {Winner}")

output_path = os.path.join("election.txt")
with open(output_path, 'w', newline='') as txtfile:
   txtfile.write(f"Total Votes: {Total_Votes}")
   txtfile.write(f"Khan: {Khan_percentage}% ({Khan})")
   txtfile.write(f"Correy: {Correy_percentage}% ({Correy})")
   txtfile.write(f"Li: {Li_percentage}% ({Li})")
   txtfile.write(f"O'Tooley: {O_Tooley_percentage}% ({Correy})")
   txtfile.write(f"Winner: {Winner}")
   txtfile.close()