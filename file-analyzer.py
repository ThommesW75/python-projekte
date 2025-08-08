"""
File Type Analyzer

This script prompts a user for a file path, checks if the file exists,
and then analyzes its extension to determine the file type.
"""

import os

# --- Get User Input ---
file_path = input("Please enter the full path to a file: ")

# --- Analyze the File ---

# First, check if the path even exists. This is our primary condition.
if os.path.exists(file_path):
    
    # This nested block only runs if the file exists.
    # Now we check the file extension using string methods.
    if file_path.endswith(".conf"):
        print(f"\nINFO: '{file_path}' is a Configuration file.")
        
    elif file_path.endswith(".log"):
        print(f"\nINFO: '{file_path}' is a Log file.")
        
    else:
        print(f"\nINFO: '{file_path}' is an Unknown file type.")

else:
    # This block runs if the path does not exist.
    print(f"\nERROR: The file '{file_path}' was not found.")