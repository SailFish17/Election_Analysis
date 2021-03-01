# Election_Analysis

## Project Overview 
A Colorado board of Elections Employee has given me the following task to complete the election audit of recent local congressional elections.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes .
3. Calculate the total number of votes each candidate recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources 
- Data source: election_results.csv
- Software: Python 3.9, Visual Studio Code

## Summary 
The analysis the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate Results were:
    - Charles Casper Stockham recieved 23.0% of the votes and 85,213 number of votes.
    - Diana DeGette recieved 73.8% of the votes and 272,892 number of votes.
    - Raymon Anthony Doane recieved 3.1% of the votes and 11,606  number of votes.
-The winner of the election was:
    - Diana DeGetter who recieved 73.8% of the votes and 272,892 number of votes.

## Challenge Overview 
- The election commission has requested some additional data to complete the audit:
    - The voter turnout for each county
    - The percentage of votes from each county out of the total count
    - The county with the highest turnout

## Challenge Summary
The voter turnout for each county:

    - Jefferson had 10.5% of votes and 38,855 people voted.
    
    - Denver had 82.8% of votes and 306,055 people voted. 
    
    - Arapahoe had 6.7% of votes and 24,801 people voted.
    
- County with the highest turnout:
    - Denver had the highest voter turnout with 82.8% of votes which is equivalent to 306,055 voters.

## Election-Audit Summary

- The following script PyPoll_Challenge.py can be modify to use for any election. We can do this in two ways with the input() function and def my_function(). At the beginning of the script
for exampe we can have file_1 = input ('file_1: ') and file_2 = input ('file_2: ') and replace the syntax with open(file_1)as election_data and with open(file_2, "w") as txt_file, 
where file_1 is the file_to_load and file_2 is file_save. The input function will generate an output in the terminal asking what is the location for file_to_load and file_to_save.
The def my_function () can also be used generate other election data while using the same script. For example (def election_test(file_1, file_2):), change the (with) statements as we did with the input() function,
can be used at the beginnging with the rest of the script below and at the end election_test("folder/election data", "folder/election data txt file"). 
