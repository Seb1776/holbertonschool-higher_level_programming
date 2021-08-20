#!/usr/bin/python3
"""Display error code"""


import urllib.error
import urllib.request
from sys import argv

if __name__ == "__main__":
    """Displasy error code"""

    url = argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            r = response.read().decode('ascii')
            print(r)
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
