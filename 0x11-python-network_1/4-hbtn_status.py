#!/usr/bin/python3
"""Fetch method"""


import requests

if __name__ == "__main__":
    """Fetch method"""

    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
