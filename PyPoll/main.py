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

    
    candidates_dict = {}

#Variables 
    for row in csv_reader:
        Voter_ID = int(row[0])
        candidate = str(row[2])
        candidates_with_votes= []
    
#Initial Values
    initial_votes = 0
    total_votes = 0

#Vote Determination
    for row in csv_reader:
        initial_votes += 1 
        total_votes = int(row[0]) #+ initial_votes
        total_votes += 1
        print(total_votes)
        
#Calculations
        vote_percentage = (total_votes / initial_votes) * 100   
        print(vote_percentage)
        
#Candiate Analysis
        for candidates in csv_reader:
            candidates_with_votes = str(row[2])
            total_votes += 1
            
            if  candidate in candidates_with_votes:
                candidates_with_votes[candidate]+=1
                candidates_with_votes.append()
                print(f'{candidates_with_votes}')


                if candidates_with_votes > 50:
                    print('{candidates_with_votes}')

output_file = os.path.join("../Analysis", "output", "new.csv")
        