#!/usr/bin/python3
"""
Script to fetch and process posts from an API.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder API and print their titles."""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder API and save them in a CSV file."""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        fieldnames = ["id", "title", "body"]
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)
