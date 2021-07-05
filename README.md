# Election_Analysis


## Overview of Election Audit
A Colorado Board of Elections has given you the following tasks to complete the election audit of a recent local congressional eletion by using Python.

1. Calculate the toal number of votes cast.
2. Get a comoplet list of candidates who received votes.
3. Caluculate the total number of votes each condidate received.
4. Calculate the percentage of votes easch candidate won. 
5. Determine the winner of the election based on popular vote. 
6. The voter turnout for each county.
7. The percentage of votes from each county out of the total count.
8. The county with the highest turnout.

## Resources
- Data Source: [election_results.csv](Resources/election_results.csv)
- software: Python 3.8.8

## Election-Audit Results
The analysis of the election, [PyPoll_Challenge.py](PyPoll_Challenge.py), shows in [election_results.txt](analysis/election_results.txt) that:

![resultcapture](Resources/election_results.png)

-  There were 369,711 votes cast in the election. 
         
         #To get total votes. 
         
         # 1.Initialize a total vote counter.
         total_votes = 0
         
            # 2.For each row in the CSV file.
            for row in reader:
         
               # 3.add to the total vote count
               total_votes = total_votes + 1
   
-  The county vote results were:
   - Jefferson had 10.5% of the vote and 38,855 votes.
   - Denver had 82.8% of the vote and 306,055 votes.
   - Arapahoe: 6.7% of the vote and 24,801 votes.

         # To get the number of total votes for each county.
         
         #  1.Create a county list and county votes dictionary.
            county_names = []
            county_votes = {}
            
               # 2. For each row in the CSV file.
               for row in reader:
               
                  # 3. Write an if statement that checks that the
                  # county does not match any existing county in the county list.
                  if county_name not in county_names:

                     # 4. Add the existing county to the list of counties.
                     county_names.append(county_name)

                     # 5. Begin tracking the county's vote count.
                     county_votes[county_name]=0

                  # 6. Add a vote to that county's vote count.
                  county_votes[county_name] += 1
                  
                  
          # To get the percentage of total votes for each county.  
           

            
- The county that had the largest number of votes:
   - Denver, which had 82.8% of the vote and 306,055 votes.
- The candidate results were:
   - Charles Casper Stockham: 23.0% (85,213)
   - Diana DeGette: 73.8% (272,892)
   - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
   - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
   
* All codes are retrieved and disected from [PyPoll_Challenge.py](PyPoll_Challenge.py)
## Election-Audit Summary
