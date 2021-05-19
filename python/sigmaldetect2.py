#!/usr/bin/python3

# Script Name: sigmaldetect.py
# Author Name: Tom Esch
# Date of Latest Revision: 5/18/21
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
    filename = input("Enter the search string : ")
    for dirpath, dirs, files in os.walk("."):  
                for filename in files:
                            fname = os.path.join(dirpath,filename)
                            with open(fname) as myfile:
                                        print(myfile.read())    

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

