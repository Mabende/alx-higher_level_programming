#!/usr/bin/python3
"""
<<<<<<< HEAD
 script that takes in a URL and an email,
 sends a POST request to the passed URL with the email as a parameter,
 and displays the body of the response (decoded in utf-8)
"""


import urllib.request
import urllib.parse
import sys


if len(sys.argv) < 3:
    print("Usage: python script_name.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Encode the email data
data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')  # Convert to bytes

req = urllib.request.Request(url, data=data, method='POST')

with urllib.request.urlopen(req) as response:
    # Decoding and displaying the body of the response
    body = response.read().decode('utf-8')
    print(body)
=======
Takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse
if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
>>>>>>> 85c830d5152b4c87b4bb23ab8ef9119fffe1b20d
