import os
import configparser
import json
import time

class CaseInsensitiveConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr  # Override optionxform to maintain case sensitivity

def convert_ini_to_json(ini_file_path, json_file_path):
    # Check if the INI file exists
    if not os.path.exists(ini_file_path):
        print("The 'presetoutfits.ini' file was not found in the directory.")
        try_again = input("Please put the 'presetoutfits.ini' file in the converter directory. Enter 'y' to retry: ")
        if try_again.lower() == 'y':
            convert_ini_to_json(ini_file_path, json_file_path)
            return
        else:
            print("Operation canceled.")
            return

    # Check if the JSON file already exists
    if os.path.exists(json_file_path):
        delete_existing = input("File 'outfits.json' already exists. Do you want to delete it? (y/n): ")
        if delete_existing.lower() == 'y':
            os.remove(json_file_path)
        else:
            print("Operation canceled.")
            return

    # Prompt user to confirm readiness to proceed
    proceed = input("Ready to proceed with conversion? (y/n): ")
    if proceed.lower() != 'y':
        print("Operation canceled.")
        return

    # Initialize an empty list to store outfit dictionaries
    outfits = []

    # Parse the ini file
    config = CaseInsensitiveConfigParser(inline_comment_prefixes='//', allow_no_value=True)
    config.read(ini_file_path)

    # Iterate over sections in the ini file
    for section in config.sections():
        outfit = {'Name': section}  # Add the section name as 'Name' field
        for option, value in config.items(section):
            if option != 'Category3':  # Skip 'Category3' field
                outfit[option] = value
        outfits.append(outfit)

    # Write the outfits list to a JSON file named 'outfits.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(outfits, json_file, indent=4)

    # Print end message
    print("Conversion Completed! Congrats on your new files! Tool made by boris")

    #
    print ("Only for use with EUP Assets")
    print ("©Visit Liberty 2023-2024")
    print ("©BorisMods 2023-2024")

    # Display countdown timer before closing
    print("Script closing in 8 seconds... have a good one!")
    for i in range(8, 0, -1):
        print(f"Closing in {i} seconds...", end='\r')
        time.sleep(1)

# Path to the input and output files
ini_file_path = 'presetoutfits.ini'
json_file_path = 'outfits.json'

# Convert the ini file to JSON
convert_ini_to_json(ini_file_path, json_file_path)
