# Modules
import csv

# Set path for file
csvpath = "Resources/budget_data.csv"


# Define variables
month_count = 0
total_profit = 0
last_month_profit = 0
changes = []
month_changes = []

print(csvpath)

# Open/read CSV file using UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read csv header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Loop through csv file
    for row in csvreader:
        
        # Total month counter
        month_count += 1

        # Total profit counter
        total_profit = total_profit + int(row[1])

        # If no change in month count
        if (month_count == 1):
            last_month_profit = int(row[1])
        # If change in month count, set last month profit and subtract it from first month profit
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            # Reset last month profit
            last_month_profit = int(row[1])

    # Calculate average profit/loss change
    avg_change = sum(changes) / len(changes)

    # Calculate max profit/loss change
    max_change = max(changes)
    max_month_index = changes.index(max_change)
    max_month = month_changes[max_month_index]

    # Calculate min profit/loss change
    min_change = min(changes)
    min_month_index = changes.index(min_change)
    min_month = month_changes[min_month_index]


    # Output analysis
    output = f"""Financial Analysis
    --------------------------------------------
    Total Months: {month_count}
    Total: ${total_profit}
    Average Change: ${round(avg_change, 2)}
    Greatest Increase in Profits: {max_month}
    Greatest Decrease in Profits: {min_month}"""

    print(output)

        







