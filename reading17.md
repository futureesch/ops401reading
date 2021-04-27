Reading17

https://www.ibm.com/cloud/learn/vpc 

“A VPC gives an enterprise the ability to define and control a virtual network that is logically isolated from all other public cloud tenants, creating a private, secure place on the public cloud.”

Public cloud is like having roommates whereas a VPC is like having a private condo. Also likened to social media account settings equivalent to “friends-only” etc.

Features: Scalability to adapt to business needs, availability via redundancy and high fault tolerance, logically isolated resources means greater security, the savings are in the cloud.

Benefits: Flexibility with servers, storage, and networks, always on for customers, reduced risk, allows SOC or CSIRT to focus on higher-level mission goals for the organization.

Architecture:
Compute - Virtual Server Instances (VSIs)
Storage - “Block storage” akin to hard drive storage
Networking - Control over public gateways, load-balancing across servers to maximize availability, routers and direct links to resources on the VPC.

Top end of the OSI

“The web or presentation tier, which takes requests from web browsers and presents information created by, or stored within, the other layers to end users.

The application tier, which houses the business logic and is where most processing takes place.

The database tier, comprised of database servers that store the data processed in the application tier.

To create a three-tier application architecture on a VPC, you assign each tier its own subnet, which will give it its own IP address range. Each layer is automatically assigned its own unique ACL.”

Security

Access control lists (ACLs): rules limiting who can access a particular subnet on the VPC. “A subnet is a portion or subdivision of your VPC; the ACL defines the set of IP addresses or applications granted access to it.”

Security group: create resources (which may be situated in more than one subnet) and assign uniform access rules to them. “For example, if you have three applications in three different subnets, and you want them all to be public Internet-facing, you can place them in the same security group. Security groups act like virtual firewalls, controlling the flow of traffic to your virtual servers, no matter which subnet they are in.”

VPC vs…

VPN - Usually just encrypts connections to public networks; VPNaaS can be included in a VPC set up.

Private Cloud - Some private clouds are publicly shared, whereas a true VPC logically separates networks from each other--it’s up to the customer to trust the CSP to actually do this.

Public Cloud - There may be limits and/or different ways of scaling that are less convenient here than in a private, logically separated space.

Pricing is modular, so it is imperative to assess network needs no differently than one would have with on-prem design.
