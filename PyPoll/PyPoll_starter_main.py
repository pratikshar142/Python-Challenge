# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll", "Resources/election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll", "analysis/election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  

# Track the total number of votes cast


# Define lists and dictionaries to track candidate names and vote counts
candidate={}

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes+=1

        # Get the candidate's name from the row
        candidate_name=row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate:
            vote_count=0

        # Add a vote to the candidate's count
        vote_count=candidate.get(candidate_name,0)
        vote_count+=1
        candidate[candidate_name]=vote_count

    print( "Election Results")
    print("\n---------------------------------------------------------------------------------------")

        
       
# Print the total vote count (to terminal)
    total_vote_output='\n'+f"Total votes:{total_votes}"
    print(total_vote_output)
    print("\n---------------------------------------------------------------------------------------")

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    
       
    # Write the total vote count to the text file
    output= "Election Results"
    output+= "\n---------------------------------------------------------------------------------------------\n"
    output+=total_vote_output
    output+= "\n---------------------------------------------------------------------------------------------\n"
    
    
    # Loop through the candidates to determine vote percentages and identify the winner
    for key,value in candidate.items():

        # Get the vote count and calculate the percentage
        percent_vote=round(((value*100)/total_votes),3)


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage
        candidate_summary='\n'+f"{key}:{percent_vote}%  ({(value)})"
        print(candidate_summary)
        output+=f"{candidate_summary}\n"


    # Generate and print the winning candidate summary
        Winner_output= max(candidate,key=candidate.get)
    print("\n---------------------------------------------------------------------------------------")
    print(f"\n Winner:{Winner_output}\n")
    print("---------------------------------------------------------------------------------------")

        
  # Write the Winning candidate to text file
    output+= "\n---------------------------------------------------------------------------------------------\n"
    output+= f"\n Winner :{Winner_output}"
    output+= "\n---------------------------------------------------------------------------------------------\n"        
    # Save the winning candidate summary to the text file
    txt_file.write(output)
    
