#!/usr/bin/env python3

# Author: Tom Esch
# Last Revised: April 12th, 2021
# Purpose: 

# Import Libraries
from cryptography.fernet import Fernet

# Generate a key and save it into a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key is "+str(key.decode('utf-8')))

# Load the key from the current directory named 'key.key'
def load_key():
    return open("key.key", "rb").read()

# Main
write_key() # Generate and write a new key
key = load_key() # Load the previously generated key
print("Key is "+str(key.decode('utf-8')))

message = "Hey budday!".encode()
print("Plaintext is "+str(message.decode('utf-8')))

f = Fernet(key) # Initialize the Fernet class

encrypted = f.encrypt(message) # Encrypt the message

# Print how it looks
print ("Ciphertext is "+str(encrypted.decode('utf-8')))




