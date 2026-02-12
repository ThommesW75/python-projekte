"""
Path Existence Checker

This script prompts a user for a file or directory path and checks
if it actually exists on the filesystem using the 'os' module.
"""

# To use functions for interacting with the OS, we must import the 'os' module.
import os

# --- Get User Input ---
# Prompt the user for a path and store it in a variable.
user_path = input("Please enter a path to check (e.g., /home/thommesw): ")

# --- Check Path and Print Result ---

# The condition: os.path.exists(user_path) will be either True or False.
if os.path.exists(user_path):
    # This block runs ONLY if the condition is True.
    print(f"\nSUCCESS: The path '{user_path}' exists.")
else:
    # This block runs ONLY if the condition is False.
    print(f"\nERROR: The path '{user_path}' was not found.")