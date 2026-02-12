"""
Bulk IP Address Checker

This script iterates over a predefined list of IP addresses and
simulates a status check for each one.
"""

# A list of IP addresses to be checked.
ips_to_check = ["8.8.8.8", "1.1.1.1", "208.67.222.222"]

# --- Start Checking Loop ---

# The for-loop takes each item from the list one by one.
# In each iteration, the current item is stored in the 'ip' variable.
for ip in ips_to_check:
    # This indented block is executed for every single IP in the list.
    print(f"Checking connection to {ip}...")

# --- Final Message ---

# This line is NOT indented, so it runs only once after the loop is complete.
print("\nAll IP addresses have been checked.")