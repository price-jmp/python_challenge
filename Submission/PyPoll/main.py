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

    # Loop through csv file and count votes
    for row in csvreader:

        # Count votes
        vote_count += 1

        # Count votes and add to dictionary
        row_candidate = row[2]
        if row_candidate in candidate_dict.keys():
            candidate_dict[row_candidate] += 1
        else:
            candidate_dict[row_candidate] = 1

# Generate header / Total Vote output
output = f"""Election Results
------------------------------
Total Votes: {vote_count}
------------------------------\n"""

# Analyze dictionary data for vote percentages, winner
max_votes = 0
max_candidate = ""

for candidate in candidate_dict.keys():
    # Count votes
    votes = candidate_dict[candidate]
    # Calculate percent
    vote_percent = (votes / vote_count) * 100

    # Generate middle output section
    candidate_info = f"{candidate}: {round(vote_percent, 3)}% ({votes})\n"
    output += candidate_info

    # Get vote max to determine winner
    if votes > max_votes:
        max_candidate = candidate
        max_votes = votes

winner = f"""------------------------------
Winner: {max_candidate}
------------------------------"""
output += winner

print(output)

# Generate output text file
with(open("pypoll_output.txt", 'w') as f):
    f.write(output)