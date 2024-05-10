#!/usr/bin/python3
<<<<<<< HEAD
"""
Fetches the URL: https://alx-intranet.hbtn.io/status
"""

from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    request = Request(url)

    with urlopen(request) as response:
        raw_content = response.read()
        decoded_content = raw_content.decode('utf-8')

        print('Body response:')
        print('\t- type: {_type}'.format(_type=type(raw_content)))
        print('\t- content: {_content}'.format(_content=raw_content))
        print('\t- utf8 content: {_utf8_c}'.format(_utf8_c=decoded_content))
=======
"""Fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
>>>>>>> 85c830d5152b4c87b4bb23ab8ef9119fffe1b20d
