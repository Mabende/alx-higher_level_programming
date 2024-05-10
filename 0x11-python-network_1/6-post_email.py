#!/usr/bin/python3
"""
<<<<<<< HEAD
script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays
the body of the response.
"""
from sys import argv
import requests


if __name__ == '__main__':
    print(requests.post(argv[1], data={'email': argv[2]}).text)
=======
Takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response
"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    r = requests.post(url, data=value)
    print(r.text)
>>>>>>> 85c830d5152b4c87b4bb23ab8ef9119fffe1b20d
