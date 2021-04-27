#!/usr/bin/env python3

# Author - Tom Esch
# Last Revised - 4/26/2021
# Ops Challenge - Automated Brute Force Wordlist Attack Tool Part 1 of 3

# Import libraries
import time, getpass

# Declare functions
def iterator ():
    filepath = input("Enter your dictionary filepath:\n")
    #filepath = ~/ops401reading/python
    
    file = open(filepath, "r")
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()

# def check_password()
def recognizer ():
    searchstring = input("Enter the string you wish to search:\n")
    source = input("Enter your dictionary filepath:\n")

    with open(source, "r") as file:

        if searchstring in file.read():
            print("\nThe search string appeared in the word list.")
        else:
            print("\nThe search string did NOT--I repeat, did NOT--appear in the word list.")
    
# Main

if __name__ == "__main__": # when my computer runs this file...do this stuff
    while True:
        mode = input("""
Brue Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            recognizer()
        elif (mode == '3'):
            break
        else:
            print("Invalid selection...") 

