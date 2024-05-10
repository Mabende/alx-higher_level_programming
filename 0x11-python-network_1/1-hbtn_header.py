#!/usr/bin/python3
"""
<<<<<<< HEAD
script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable
found in the header of the response.
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.getheader("X-Request-Id")
        print(f"{html}")
=======
Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        request_id = response.getheader("X-Request-Id")
    print(request_id)
>>>>>>> 85c830d5152b4c87b4bb23ab8ef9119fffe1b20d
