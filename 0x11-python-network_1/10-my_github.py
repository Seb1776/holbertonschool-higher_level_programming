#!/usr/bin/python3
"""Method to get Github's API"""


import requests
from sys import argv

if __name__ == "__main__":
    """Get Github's API"""

    data = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print(data.json().get('id'))
