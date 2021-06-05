write a program to build a calculator using python
write a program to check input string is palendrom
# you are given a list cpdomains of count-paired domains.
# would like a list of count-paired domains, that explicitly counts the number of visits to each subdomain.
# Input:
# ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output:
# ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
# Explanation:
# We will visit
# "google.mail.com" 900 times,
# "yahoo.com" 50 times,
# "intel.mail.com" once
# "wiki.org" 5 times.
#
# For the subdomains, we will visit
# "mail.com" 900 + 1 = 901 times,
# "com" 900 + 50 + 1 = 951 times,
# "org" 5 times.
