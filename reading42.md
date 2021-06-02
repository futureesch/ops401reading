https://www.varonis.com/blog/what-is-mimikatz/

How Do You Use Mimikatz
When you run Mimikatz with the executable, you get a Mimikatz console in interactive mode where you can run commands in real time.

Run Mimikatz as Administrator: Mimikatz needs to be “Run as Admin” to function completely, even if you are using an Administrator account.

Checking Version of Mimikatz

There are 2 versions of Mimikatz: 32bit and 64bit. Make sure you are running the correct version for your installation of Windows. Run the command ‘version’ from the Mimikatz prompt to get information about the Mimikatz executable, the Windows version, and if there are any Windows settings that will prevent Mimikatz from running correctly.

Extracting clear text passwords from memory

The  module sekurlsa in Mimikatz lets you dump passwords from memory. 
To use the commands in the sekurlsa module, you must have Admin or SYSTEM permissions.

First, run the command:
mimikatz # privilege::debug

The output will show if you have appropriate permissions to continue.

Next, start the logging functions so you can refer back to your work.
mimikatz # log nameoflog.log

And finally, output all of the clear text passwords stored on this computer.
mimikatz # sekurlsa::logonpasswords

Using Other Mimikatz modules
The crypto module allows you to access the CryptoAPI in Windows which lets you list and export certificates and their private keys, even if they’re marked as non-exportable.

The kerberos module accesses the Kerberos API so you can play with that functionality by extracting and manipulating Kerberos tickets.

The service module allows you to start, stop, disable, etc. Windows services.

The coffee command returns ascii art of coffee. 

