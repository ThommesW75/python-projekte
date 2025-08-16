"""
IP Whitelist Checker

This script validates if a user-provided IP address exists in a predefined
set of allowed IPs.
"""

# A set of allowed IP addresses. A set is used because it's fast
# and automatically handles uniqueness.
whitelist = {"192.168.1.100", "10.0.5.23", "172.16.31.5"}

# Get the IP address to check from the administrator
ip_to_check = input("Please enter the IP address to validate: ")

# Check if the provided IP is a member of the whitelist set
if ip_to_check in whitelist:
    print(f"\nSUCCESS: The IP address '{ip_to_check}' is on the whitelist.")
else:
    print(f"\nWARNING: The IP address '{ip_to_check}' is NOT on the whitelist.")