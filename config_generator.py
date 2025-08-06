"""
Config Generator for a monitoring service.

This script prompts an administrator for a server hostname and a port
and then prints a formatted configuration line.
"""

# --- Get User Input ---

# Prompt for the hostname and store the result in the 'hostname' variable
hostname = input("Please enter the server hostname: ")

# Prompt for the port and store the result in the 'port' variable
port = input("Please enter the port to monitor: ")


# --- Generate and Print Output ---

# Use an f-string to combine the static text with the variable values.
# The {} are placeholders for the content of the variables.
print(f"\nSUCCESS: Monitoring configured for {hostname} on port {port}.")