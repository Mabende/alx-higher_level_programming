#!/usr/bin/python3
"""
<<<<<<< HEAD
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        user_info = response.json()
        print(user_info.get("id"))
    else:
        print("Not a valid JSON")
=======
Takes your GitHub credentials (username and password) and uses the
GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
>>>>>>> 85c830d5152b4c87b4bb23ab8ef9119fffe1b20d
