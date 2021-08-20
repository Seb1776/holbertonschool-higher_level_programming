#!/usr/bin/python3
"""Send a POST"""


import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    """Send POST"""
    url = argv[1]
    arg = {"email": argv[2]}
    mail = urllib.parse.urlencode(arg).encode('ascii')

    req = urllib.request.Request(url, mail)

    with urllib.request.urlopen(req) as response:
        r = response.read().decode('utf-8')
        print(r)
