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
    votes = 0

    #dictionary of candidates
    candidates_with_votes = {}

    for Candidates in csv_reader:
    votes += 1
        #for row in csv_reader:
        #Voter_ID = row[0]
        #County = row[1]
        #Candidate = row[2]    
        #Voter_ID = float(Voter_ID)
         


