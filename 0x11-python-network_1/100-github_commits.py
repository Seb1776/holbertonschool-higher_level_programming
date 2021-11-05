#!/usr/bin/python3
"""Script that lists 10 commits"""

import requests
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)

    request = requests.get(url)
    request = request.json()
    for i in range(10 if len(request) > 10 else len(request)):
        author = request[i].get('commit').get('author').get('name')
        sha = request[i].get('sha')
        print("{}: {}".format(sha, author))
