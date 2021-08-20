#!/usr/bin/python3
"""Fetch request"""


import urllib.request
from sys import argv

if __name__ == "__main__":
    """Attempt to fetch request"""
    url = argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        r = response.headers
        print(r["X-Request-Id"])
