#!/usr/bin/python3
"""Post Email"""


import requests
from sys import argv

if __name__ == "__main__":
    """Post Email"""

    url = argv[1]
    mail = {"email": argv[2]}

    req = requests.post(url, mail)
    print(req.text)
