#!/usr/bin/env python3

# Author: Tom Esch
# Last Revised: April 7th, 2021
# Purpose: Ping Drop Alert

# Look up how to wrap PW in an environmental variable
#  mxtoolbox.com

#Import Libraries 
import smtplib,subprocess,time

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

# To be continued...

server = smtplib.SMTP_SSL("smtp.gmail.com," 465) # Server I'm sending from
server.ehlo()

server.login("attackwithcare@gmail.com", "xxxxaaaaa") # Login to the server

msg = "The host status has changed: it is DOWN"
server.sendmail("attackwithcare@gmail.com", "tom@tomeschmusic.com", msg)
server.quit() # Send email for UP to DOWN 

msg = "The host status has changed: it is UP"
server.sendmail("attackwithcare@gmail.com", "tom@tomeschmusic.com", msg)
server.quit() # Send email for DOWN to UP
