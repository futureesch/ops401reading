# Purpose - Automated Group Policy Hardening 
# Author - Tom Esch
# Date last revised - April 8th, 2021

# Enable Password Complexity
Set-ADDefaultDomainPasswordPolicy -ComplexityEnabled $true -Identity corp.initrobe.com

# Implementing remediation 1.1.5 (L1)
Set-ADDefaultDomainPasswordPolicy -MinPasswordLength 7 -Identity corp.initrobe.com

# Implementing remediation 18.3.2 (L1)
Disable-WindowsOptionalFeature -Online -FeatureName smb1protocol
