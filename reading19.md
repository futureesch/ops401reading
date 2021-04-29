Reading19

https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html 

“Amazon GuardDuty is a continuous security monitoring service that analyzes and processes the following Data sources: VPC Flow Logs, AWS CloudTrail management event logs, Cloudtrail S3 data event logs, and DNS logs. It uses threat intelligence feeds, such as lists of malicious IP addresses and domains, and machine learning to identify unexpected and potentially unauthorized and malicious activity within your AWS environment. This can include issues like escalations of privileges, uses of exposed credentials, or communication with malicious IP addresses, or domains. For example, GuardDuty can detect compromised EC2 instances serving malware or mining bitcoin. It also monitors AWS account access behavior for signs of compromise, such as unauthorized infrastructure deployments, like instances deployed in a Region that has never been used, or unusual API calls, like a password policy change to reduce password strength.”

Regular AWS Root account for access to GuardDuty; may invite other accounts and operate as administrator and the added accounts become members allowing for unique configuration for up to 1000 profiles per account. 

Detectors are GuardDuty findings by region with an identifying tag You can implement Suppression Rules to filter the data reporting for segmentation of activity about and for those who need it when they need it. 
