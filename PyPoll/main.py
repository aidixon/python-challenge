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

    #vote count
    initial_votes = 0
    

    #dictionary of candidates
    candidates_with_votes_dict= {}

    #voter analysis 
    for row in csv_reader:
        Voter_ID = int(row[0]) #+ int(initial_votes)
        Voter_ID = float(Voter_ID)
        votes = Voter_ID #+= 1 #+ initial_votes
        votes += 1
        

        #County
        County = str(row[1])
        
        #Candiate analysis
        Candidate = str(row[2])
        

        #votes = Voter_ID + votes
        print(f'TOTAL number of votes: {int(initial_votes)}')
        
         


