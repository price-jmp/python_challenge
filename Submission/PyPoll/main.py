# Modules
import csv

# Set filepath
csvpath = "Resources/election_data.csv"

# Set variables
vote_count = 0
candidate_dict = {}

# Open/read csv file using UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    # Read csv header
    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")