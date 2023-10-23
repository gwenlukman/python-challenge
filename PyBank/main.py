import os
# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)


    months = []
    total = 0
    monthly_changes = []
    monthly_profits = []

    # Looping through the CSV to find the total months, total and putting it on a list
    for row in csvreader:
        months.append(str(row[0]))
        total = total + int(row[1])
        monthly_profits.append(int(row[1]))

# Looping through the monthly_profits list to substract the profit of the next month and putting the results in a list
for profit in range(len(monthly_profits)-1):
    monthly_changes.append(monthly_profits[profit + 1]-monthly_profits[profit])

#Finding the average of monthly_changes
average = sum(monthly_changes)/len(monthly_changes)

max_change = 0
min_change = float('inf')
max_month = 0
min_month = 0

#Finding the max, min and its index to find the month of the max and min
for i in range(len(monthly_changes)):

    if monthly_changes[i] > max_change:
        max_change = monthly_changes[i]
        max_month = i

    if monthly_changes[i] < min_change:
        min_change = monthly_changes[i]
        min_month = i

print("Financial Analysis")
print('----------------------------') 
print(f"Total Months: {len(months)}")
print(f'Total: ${total}')
print(f"Average Change: ${round(average, 2)}")
print(f"Greatest Increase in Profits: {months[max_month+1]} (${max_change})")
print(f"Greatest Decrease in Profits: {months[min_month+1]} (${min_change})")


    
