#!/usr/bin/python3
"""
<<<<<<< HEAD
error code
"""

import urllib.request
import urllib.error
import sys


if len(sys.argv) < 2:
    print("Usage: python script_name.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Decoding and displaying the body of the response
        body = response.read().decode('utf-8')
        print(body)

except urllib.error.HTTPError as e:
    # Handling HTTPError exceptions and printing the error code
    print(f"Error code: {e.code}")
=======
Takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.error
if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
>>>>>>> 85c830d5152b4c87b4bb23ab8ef9119fffe1b20d
