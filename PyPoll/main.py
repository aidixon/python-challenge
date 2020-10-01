#importing csv file
import os
import csv

#extracting the file path
polls_csv = os.path.join("Resources", "election_data.csv")

#read file and skip header
with open ("Resources/election_data.csv", newline='') as file:
    csv_reader=csv.reader(file, delimiter=",")
    header=next(csv_reader)

