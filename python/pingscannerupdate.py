#!/usr/bin/env python3

# Author: Tom Esch
# Last Revised: April 6th, 2021
# Purpose: Ping Status Email Alert

# Look up how to wrap PW in an environmental variable
#  mxtoolbox.com

#Import Libraries 
import smtplib,subprocess,time,getpass

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

def send_downAlert():
    now = datetime.datetime.now()
    timestamp = now.strftime('%m-%d-%Y %H:%M:%S %p')  
    server = smtplib.SMTP_SSL("smtp.gmail.com," 465) # Server I'm sending from
    server.ehlo()
    server.login(email, password)
    ms2 = "Look out!!! \nYour connection is DOWN.\n %s % timestamp"
    server.sendmail('attackwithcare@gmail.com', email, msg2)
    server.quit()

def send_downAlert():
    now = datetime.datetime.now()
    timestamp = now.strftime('%m-%d-%Y %H:%M:%S %p')  
    server = smtplib.SMTP_SSL("smtp.gmail.com," 465) # Server I'm sending from
    server.ehlo()
    server.login(email, password)
    ms2 = "Look out!!! \nYour connection is DOWN.\n %s % timestamp"
    server.sendmail('attackwithcare@gmail.com', email, msg2)
    server.quit()

while True:
    scanner()


