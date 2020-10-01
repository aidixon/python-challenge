#importing csv file
import os
import csv

#extracting the file path
bank_csv = os.path.join("Resources", "budget_data.csv")

#read file, print header, skip header
with open ("Resources/budget_data.csv", newline='') as file:
    csv_reader=csv.reader(file, delimiter=",")
    csv_header=next(csv_reader)
    print(f"csvheader:{csv_header}")

#print(bank_csv)

    #Totalmonths