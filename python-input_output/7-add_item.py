#!/usr/bin/python3
"""
Script that adds command-line arguments to a list
and saves them to a JSON file.
"""

import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except (FileNotFoundError, json.JSONDecodeError):
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
