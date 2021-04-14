#!/usr/bin/env python3

# 1 of 3 Encryption Automation
# Author - Tom Esch
# Last Revised - April 13th, 2021

from cryptography.fernet import Fernet

# Prompt the user to select a mode - pull down your MENU script
# If mode 1 or 2 prompt user to proivde a filepath to a target file
# If mode 3 or 4 prompt user to provide a cleartext string

# Declaration of Variables
y_n="y"

# Declaration of Functions

# Generates a key and save it into a file
def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
      key_file.write(key)
    

# Load the key from the current directory named 'key.key'
def load_key():
    return open("key.key", "rb").read()

def encrypt_msg():
  user_msg = input("Please enter the message for encryption:")
  message_n = user_msg.encode()
  f = Fernet(key)
  encrypted = f.encrypt(message_n)
  print("Your message:")
  print(encrypted).decode()

def decrypt_msg():
  user_msg = input("Please enter the message for decryption:")
  message_d = str.encode(user_input)
  f = Fernet(key)
  decrypted = f.decrypt(message_d)
  print("Your message:")
  print(str(decrypted).decode[2:-1])

def encrypt_file():
  f = Fernet(key)
  filename = input("Please enter the filepath for a file to encrypt:")
  with open(filename, "rb") as file: 
    file_data = file.read
  with open(filename, "wb") as file:
    file.write(encrypted)

def dencrypt_file():
  f = Fernet(key)
  filename = input("Please enter the filepath for a file to dencrypt:")
  with open(filename, "rb") as file: 
    file_data = file.read
  with open(filename, "wb") as file:
    file.write(dencrypted)

def menu():
    mode = input("Welcome to EnDecrypto! Please Select: \nMode 1 to Encrypt a file 
\nMode 2 to Decrypt a file \nMode 3 to Encrypt a message \nMode 4 to Decrypt a 
message \n ") 
    if (mode=='1'):     
      encrypt_file()
      print ("...encryption complete.") 
    elif (mode=='2'):
      dencrypt_file() 
      print ("...decryption complete.")
    elif (mode=='3'):
      encrypt_msg()
      print ("...message encrypted.") 
    elif (mode=='4'): 
      decrypt_msg()
      print ("...message decrypted.")
    else: 
      print ("Unknown Option Selected!") 

# Main
write_key()

key = load_key()

while True:
  menu()
  y_n = input("To continue, press yes, to exit, press n")
  if y_n ==("n"):
    print("Farewell.")
    break
