# # Assign a variable for the file to load and the path.
# # file_to_load = 'Resources/election_results.csv'
# # # Open the election results and read the file.
# # # election_data = open(file_to_load, 'r')
# # # election_data.close()
# # file_to_load = os.path.join("Resources", "election_results.csv")

# #     print(election_data)
# # import csv and os module
# import csv
# import os 

# file_to_load = os.path.join("Resources", "election_results.csv")

# with open(file_to_load) as election_data:
#     print(election_data)

# # Create a filename  variable to direct or indirect path to file

# file_to_save =os.path.join('analysis', 'election_analysis.txt')

# # Using the open() function with the "w" mode we will write data to the file.
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#    file_reader = csv.reader(election_data)
# for row in file_reader:
#          print(row)


# # To do: read and analyze the data here

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

#Winning candidate and wining count tracker
winning_candidate= ""
winning_count= 0
winning_percentage= 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

            # Add a vote to thats candidate count 
        candidate_votes[candidate_name] += 1

    # Iterate through candidate list 
    for candidate_name in candidate_votes:
        # retrieve vote count of candidate 
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes 
        voting_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count) and (voting_percentage > winning_percentage):
            winning_count= votes
            winning_percentage= voting_percentage
            winning_candidate= candidate_name

        print(f"{candidate_name}: {voting_percentage:.1f}% ({votes:,})\n")

        #testing 
