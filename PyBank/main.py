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

#variables
    month = []
    profit_change = []
    profit = []

#inital values
    net_profit = 0
    profit_for_current_month = 0
    profit_for_previous_month = 0
    change_in_profit = 0
    first_month = 0

#defining columns 
    for row in csv_reader:
        Date = str(row[0])
        Profit_Losses = int(row[1])
        
#Creating variables for Months
        first_month +=1
        profit_for_current_month = int(Profit_Losses)
        net_profit += int(Profit_Losses)
        month.append(Date)
        if first_month > 1:

#Profit for months 
            change_in_profit = profit_for_current_month - profit_for_previous_month
            profit_change.append(change_in_profit)

#Calulations 

            max_increase = max(profit_change) + 1
            max_decrease = min(profit_change) + 1
            profit_change_sum = sum(profit_change)
            average = profit_change_sum / (change_in_profit)
            profit_for_previous_month = profit_for_current_month