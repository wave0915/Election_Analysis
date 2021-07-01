import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

       # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print the file object.
    for row in file_reader:
        print(row)

#Using the with statement open the file as a text
with open(file_to_save, "w") as txt_file:

    #Wirte some data to the file.
    txt_file.write("Hello World")

#close the file
election_data.close()
file_to_save.close()
