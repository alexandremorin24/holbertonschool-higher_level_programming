#!/usr/bin/python3
"""
Module to convert a CSV file to a JSON file.
"""

import csv
import json


def convert_csv_to_json(csv_input):
    """
    Converts a CSV file to a JSON file named 'data.json'.
    Returns: bool: True if conversion is successful, False otherwise.
    """
    data = []

    try:
        with open(csv_input, encoding="utf-8") as file:
            csvReader = csv.DictReader(file)

            for row in csvReader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_input}' not found.")
        return False

    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
