# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os
import sys

# Files to load and output (update with correct file paths)

file_to_load = os.path.join("PyBank", "Resources/budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank", "analysis/budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
change = 0
total_change = 0
avg_change = 0


greatest_increase = -sys.maxsize - 1
greatest_increase_date = None

greatest_decrease = sys.maxsize
greatest_decrease_date = None

# Open and read the csv
with open(file_to_load, 'r') as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    # Track the total and net change

    prev_row = None
    # Process each row of data
    for i, row in enumerate(reader):
       
        # Total Months
        total_months += 1

        # Track the total
        pnl = int(row[1])
        total_net += pnl

        # Track the net change
        if i > 0:  # Skip the first row (no previous row to compare to)
            prev_pnl = int(prev_row[1])
            change = pnl - prev_pnl
            total_change += change
        # Calculate the greatest increase in profits (month and amount)
        if change >= greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]
                        

        # Calculate the greatest decrease in losses (month and amount)
        if change <= greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]
       
        # set the previous row for next iteration
        prev_row = row  


# Calculate the average net change across the months
avg_change = round(total_change / (total_months - 1), 2)


# Generate the output summary
output = "Financial Analysis"
output += '\n'
output += '\n'+"------------------------------------"
output += '\n'+ f"Total Months: {total_months}"
output += '\n'+ f"Total: ${total_net}"
output += '\n'+ f"Average Change: ${avg_change}"
output += '\n'+ f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})"
output += '\n'+ f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"

# Print the output
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
