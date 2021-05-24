Reading 36

https://portswigger.net/web-security/cross-site-scripting 

Cross-Site Scripting

Reflected - when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way.
Stored - when an application receives data from an untrusted source and includes that data within its later HTTP responses in an unsafe way
DOM-Based - arises when an application contains some client-side JavaScript that processes data from an untrusted source in an unsafe way, usually by writing the data back to the DOM.

Use Cases:
Impersonate or masquerade as the victim user.
Carry out any action that the user is able to perform.
Read any data that the user is able to access.
Capture the user's login credentials.
Perform virtual defacement of the web site.
Inject trojan functionality into the web site.

Impact can be minimal to critical, depending on the application and data in play.

Finding and Testing can be done with Burp Suite’s web vulnerability scanner

Content Security Policy - a browser mechanism intended to reduce XSS impact and/or vulnerabilities. 

Dangling markup injection - captures data cross-domain through CSRF tokens that can be used to perform unauthorized actions on behalf of the user.

Prevention: 
Filter input
Encode data going out
Use appropriate response headers
Content Security Policy

Commonality of vulnerabilities? Common and probably most frequently occurring
Commonality of attacks? Stats are murky; probably less frequent exploitation than other vulnerabilities

XSS causes a website to return malicious script; CSRF involves social engineering

XSS is client-side vulnerability targeting of other application users, SQL is a server-side vulnerability targeting the application’s database

XSS prevention in PHP - Filter inputs with a whitelist of allowed characters, using type hints and type casting.

XSS prevention in Java - Filter inputs with a whitelist of allowed characters, and use a library such as google Guava for HTML and JS encoding.
