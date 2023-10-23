import os
# Import modules for reading CSV file
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable 
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Setting counts
    votes = 0
    charles = 0
    diana = 0
    raymon = 0

    # Counting how many votes each candidates get
    for row in csvreader:
        votes = votes + 1

        if row[2] == "Charles Casper Stockham":
            charles = charles + 1
        elif row[2] == "Diana DeGette":
            diana = diana + 1
        elif row[2] == 'Raymon Anthony Doane':
            raymon = raymon + 1

    # Finding the winner by who got the most votes
    if charles > diana and charles > raymon:
        winner = 'Charles Casper Stockham'
    elif diana > charles and diana > raymon:
        winner = 'Diana Degette'
    elif raymon > charles and raymon > diana:
        winner = 'Raymon Anthony Doane'
    
    #calculating the percentage
    pcharles = round(charles/votes*100, 3)
    pdiana = round(diana/votes*100, 3)
    praymon = round(raymon/votes*100, 3)

    # Printing Everything
    print('Election Results\n-------------------------')
    print(f'Total Votes: {votes}\n-------------------------')
    print(f"Charles Casper Stockham: {pcharles}% ({charles})")
    print(f"Diana Degette: {pdiana}% ({diana})")
    print(f'Raymon Anthony Doane: {praymon}% ({raymon})\n-------------------------')
    print(f'Winner: {winner}\n-------------------------')

