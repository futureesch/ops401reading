Reading 28

https://resources.infosecinstitute.com/topic/ethical-hacking-log-tampering-101/ 

Attackers seek to avoid detection. 

Disable - via command line using AuditPol, this provides a lay of the land to see what the set up is to disable
Clearing - clearlogs.ext -sec 
“Please note — if the hacker does not remove clearlogs.exe, it will serve as hard evidence of log tampering. If this occurs in a Windows 10 system or Windows Server 2016, event ID 1102(S) will be displayed as an event, and overlooking this is a common error many beginner hackers make.” 
Metasploit add-on MeterPreter
Windows Event Viewer would need to be cleared as well since log clearing creates events
In Linux - Shred -vfzu auth.log
Modifying - G.I. Joe “Knowing Is Half the Battle”
Erasing - Bash saves commands, so you’d have to clear those as well!
