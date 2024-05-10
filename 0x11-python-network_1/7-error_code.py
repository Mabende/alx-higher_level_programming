#!/usr/bin/python3
"""
<<<<<<< HEAD
script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import requests
import sys


if len(sys.argv) < 2:
    print("Usage: python script_name.py <URL>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)

if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print(response.text)
=======
Takes in a URL, sends a request to the URL and displays
the body of the response
"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
>>>>>>> 85c830d5152b4c87b4bb23ab8ef9119fffe1b20d
