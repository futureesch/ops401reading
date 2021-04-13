Reading05

https://www.jscape.com/blog/implementing-the-cia-triad-when-transferring-files-through-the-internet 

Applying the CIA triad

Confidentiality - Encryption

Data-in-transit encryption - usually achieved through solutions like SSL (e.g. FTPS, HTTPS, WebDAVs) or SSH (e.g. SFTP). 

Data-at-rest encryption - usually achieved through OpenPGP or other disk-level or file-level encryption solutions. 

Encrypting data before (while in the sender's server), during (while traversing the network), and after (upon arrival at the recipient's server) a file transfer = end-to-end encryption.”

2 Factor Authentication

Integrity

Data integrity = use hash functions and digital signatures

High Availability Cluster  
Setting up one or more failover server(s) that can immediately take over should the primary server go down. This is known as an active-passive high availability configuration.
Set up two or more server (s) in such a way that they are both active servers. This is known as an active-active high availability configuration. The main purpose of an active-active HA configuration is to distribute the workload and reduce the chance of a server from going down due to overload. 

The rest is a pitch to get jscape to deploy all of these under one roof.

https://www.howtogeek.com/67241/htg-explains-what-are-md5-sha-1-hashes-and-how-do-i-check-them/ 

Run the hash function to confirm the real, original file hasn’t been corrupted during the download process. Even a small change to the file will dramatically change the hash.

“collisions” have been found with the MD5 and SHA-1 functions. These are multiple different files—for example, a safe file and a malicious file—that result in the same MD5 or SHA-1 hash. Prefer SHA-256 when possible.
Good reminders for how to compare hashes across Windows, Mac, and Linux (they look the same across OS platforms, just different access terminology).

Great way to verify the authenticity of a file--and its integrity in tact

