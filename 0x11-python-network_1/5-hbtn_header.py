#!/usr/bin/python3
"""Fetch header"""


import requests
from sys import argv

if __name__ == "__main__":
    """Fetch header"""

    url = argv[1]
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
