#!/usr/bin/env python
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def adds_all_arguments ():
    try:
        existing_data = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_data = []
    existing_data.extend(arguments)
    save_to_json_file(existing_data, 'add_item.json')

if __name__ == "__main__":
    arguments = sys.argv[1:]

    if not arguments:
        print("Usage: python script.py arg1 arg2 arg3 ...")
        sys.exit(1)

    add_arguments_and_save(arguments)

    print(f"Arguments added and saved to 'add_item.json'")
