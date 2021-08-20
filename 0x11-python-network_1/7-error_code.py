#!/usr/bin/python3
"""Error Code"""


import requests
from sys import argv

if __name__ == "__main__":
    """Error Code"""

    url = argv[1]
    req = requests.get(url)

    if req.status_code == 200:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
