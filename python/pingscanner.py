#!/usr/bin/env python3

# Author: Tom Esch
# Last Revised: April 6th, 2021
# Purpose: Ping Scanner
    # Evaluate the response as either success or failure.
    # Assign success or failure to a status variable.
    # For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
        # Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

import subprocess
import time

def scanner():
    for ping in range(1):
        address = "192.168.1.20" 
        res = subprocess.call(['ping', '-c', '1', address])
        print("Start : %s" % time.ctime())
        if res == 0:
            print("ping to", address, "success!")
        elif res == 2:
            print("no response from", address)
        else:
            print("ping to", address, "failed!")
    time.sleep(2)

while True:
    scanner()

# Fin
