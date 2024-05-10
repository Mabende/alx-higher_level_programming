#!/usr/bin/python3
<<<<<<< HEAD
"""
fetches a link
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

if response.status_code == 200:
    print('Body response:')
    print('\t- type: {_type}'.format(_type=type(response.text)))
    print('\t- content: {_content}'.format(_content=response.text))
else:
    print(f"Failed to fetch the URL. Status code: {response.status_code}")
=======
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests
if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
>>>>>>> 85c830d5152b4c87b4bb23ab8ef9119fffe1b20d
