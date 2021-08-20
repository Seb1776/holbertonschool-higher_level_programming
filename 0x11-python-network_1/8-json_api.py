#!/usr/bin/python3
"""JSON API"""


import requests
from sys import argv

if __name__ == "__main__":
    """JSON API"""

    url = "http://0.0.0.0:5000/search_user"

    if len(argv) > 1:
        data = {"q": argv[1]}

    else:
        data = {"q": ""}

    req = requests.post(url, data=data)

    try:
        json_response = req.json()

        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
