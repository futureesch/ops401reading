Reading09

https://www.ssh.com/academy/pki 

PKI - is Public Key Infrastructure.  authenticating users and devices The trusted party signing the document associating the key with the device is called a certificate authority (CA). The certificate authority also has a cryptographic key that it uses for signing these documents. These documents are called certificates.

Public key cryptography - an asymmetric form of cryptography - Public keys are issued for users to encrypt data to return to the originator of the key pair. This originator has the private key needed to decrypt data encrypted using the paired public key.

Most public key infrastructures use a standardized machine-readable certificate format for the certificate documents. The standard is called X.509v3. Originally, it was an ISO standard, but these days it is maintained by the Internet Engineering Task Force as RFC 3280.

Most public key infrastructures use a standardized machine-readable certificate format for the certificate documents. The standard is called X.509v3. Originally, it was an ISO standard, but these days it is maintained by the Internet Engineering Task Force as RFC 3280.

The Secure Shell protocol supports certificates for authenticating hosts and users. Tectia SSH uses standards-based X.509 certificates, whereas OpenSSH uses its own proprietary certificate formats.

Limitations:

Weakness of public PKI 
Any certificate authority can sign a certificate for any person or computer. 
Certificate authorities in countries, some authoritarian or even potentially hostile governments. 
Sometimes certificate authorities create or are coerced to create certificates for parties they have no business vouching for.

Intelligence agencies can use fraudulent certificates for espionage, malware injection, and forging messages or evidence to disrupt or discredit adversaries. Only limited trust should be placed on certificates from public certificate authorities.

Some organizations have and operate prive PKIs using their own internal certificate authority. Potentially more secure, but potentially at a cost.

“SSH Communications Security was one of the early pioneers in PKI. We participated in the standardization work for X.509v3 and proposed an alternative approach called Simple Public Key Infrastructure (SPKI) to address some of the trust issues with the X.509 standard. We wrote some of the standards documents on certificate enrollment protocols. We were also selling an advanced certificate authority product called SSH Certifier from 2001 onwards. Among other things, it pioneered support for multiple certificate authorities and multiple registration authorities in the same system and using customizable policy rules for choosing the certificate authority to obtain a certificate from. For more information, see SSH's contributions to PKI and Certificate management.”
