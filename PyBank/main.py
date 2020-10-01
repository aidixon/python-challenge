#importing csv file
import os
import csv

#extracting the file path
bank_csv = os.path.join("Resources", "budget_data.csv")

#read file and skip header
with open ("Resources/budget_data.csv", newline='') as file:
    csv_reader=csv.reader(file, delimiter=",")
    header=next(csv_reader)

print(bank_csv)

    #Totalmonths=0
    count = []
    monthcount = 0


#for row in 
#