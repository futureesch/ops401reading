Reading 29

https://owasp.org/www-community/Application_Threat_Modeling 


Threat Models include:
A description / design / model of what you’re worried about
A list of assumptions that can be checked or challenged in the future as the threat landscape changes
A list of potential threats to the system
A list of actions to be taken for each threat
A way of validating the model and threats, and verification of success of actions taken

4 Questions

What are we building? As a starting point you need to define the scope of the Threat Model. 

What can go wrong? This is a “research” activity in which you want to find the main threats that apply to your application. There are many ways to approach the question, including brainstorming or using a structure to help think it through. Structures that can help include STRIDE, Kill Chains, CAPEC and others.

What are we going to do about that? Produce outputs from the model which are actionable.

Did we do a good enough job? Assess, assess, assess.

When to Threat Model
When the system changes, you need to consider the security impact of those changes. Sometimes those impacts are not obvious.

Threat modeling integrates into Agile by asking “what are we working on, now, in this sprint/spike/feature?”

https://www.ockam.io/learn/blog/introduction_to_STRIDE_security_model 

Spoofing - Fake IDs
Tampering - Grocery store packaging
Repudiation - Trace attempts and rejects endless login attempts (brute force)
Information Disclosure - confidentiality, integrity, accessibility
Denial of Service - Spamming servers to prevent legitimate users access
Elevation of Privilege - spoofing is authentication, and this is for authorization.
