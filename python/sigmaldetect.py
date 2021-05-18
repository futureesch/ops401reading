#!/usr/bin/python3

# Script Name: sigmaldetect.py
# Author Name: Tom Esch
# Date of Latest Revision: 5/17/21
# Purpose: User Prompted Malware Detection Tool

# Prompt the user to type in a file name to search for.
# Prompt the user for a directory to search in.
# Search each file in the directory by name
# For each positive detection, print to the screen the file name and location.
# At the end of the search process, print to the screen how many files were searched and how many hits were found.

# import libraries
import os

# Declaration of Functions:

# def = modewindows():

def modelinux():
# Ask the user to enter string to search
    search_path = input("Enter directory path to search : ")
    file_type = input("File Type : ")
    search_str = input("Enter the search string : ")

    # Append a directory separator if not already present
    if not (search_path.endswith("/") or search_path.endswith("\\") ): 
            search_path = search_path + "/"

    # If path does not exist, set search path to current directory
    if not os.path.exists(search_path):
            search_path ="."

    # Repeat for each file in the directory  
    for fname in os.listdir(path=search_path):

       # Apply file type filter   
       if fname.endswith(file_type):

            # Open file for reading
            fo = open(search_path + fname)

            # Read the first line from the file
            line = fo.readline()

            # Initialize counter for line number
            line_no = 1

            # Loop until EOF
            while line != '' :
                    # Search for string in line
                    index = line.find(search_str)
                    if ( index != -1) :
                        print(fname, "[", line_no, ",", index, "] ", line, sep="")

                    # Read next line
                    line = fo.readline()  

                    # Increment line counter
                    line_no += 1
            # Close the files
            fo.close()

      
# Main

if __name__ == "__main__": # when my computer runs this file...do this s
    while True:
        mode = input("""
Welcome to the Signature Malware Detector Tool !!! 
1 - Windows Detection Unit
2 - Linux Detection Unit
3 - Exit and return to prompt
    Please enter a number: 
""")
        if (mode == "1"):
            modewindows()
        elif (mode == "2"):
            modelinux()
        elif (mode == "3"):
            break                   
        else:
            print("Invalid selection...") 

# Fin for now.
