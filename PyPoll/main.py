#importing csv file
import os
import csv

#extracting the file path
polls_csv = os.path.join("Resources", "election_data.csv")

#read file, print header, skip header
with open ("Resources/election_data.csv", newline='') as file:
    csv_reader=csv.reader(file, delimiter=",")
    csv_header=next(csv_reader)
    print(f"csvheader:{csv_header}")

#Variables 
    #for row in csv_reader:
        #Voter_ID = int(row[0])
        #candidate = str(row[2])
    candidates_with_votes= []
    
#Initial Values
    initial_votes = 0
    total_votes = 0

#Vote Determination
    for row in csv_reader:
        initial_votes += 1 
        total_votes = int(row[0]) + initial_votes
        total_votes += 1
        break
        print(f'TOTAL number of votes: {(total_votes)}')
        
#Calculations
    vote_percentage = total_votes / initial_votes    
        
#Candiate Analysis
    for candidates in csv_reader:
        candidates_with_votes = str(row[2])
        total_votes += 1
            
    if candidates_with_votes in candidates:
        candidates_with_votes[candidates]+=1
        candidates_with_votes.append()
        print(f'{candidates_with_votes} is the winner')
        


    if vote_percentage >= 50:
        print(candidates)

        