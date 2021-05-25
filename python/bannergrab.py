#!/usr/bin/env python3 

# Purpose - Web Application Fingerprinter
# Author - Tom Esch
# Last Revised - 5/24/2021

def bannergrab():
        target = input("[*]Enter the URL or IP of the target: ") # Prompts the user to type a URL or IP address.
        port = input("[*]Designate the target's port to fingerprint: ") # Prompts the user to type a port number.
       
# Main
        
bannergrab()

# Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.

# Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.

# Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.
