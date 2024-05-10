#!/usr/bin/python3
"""
<<<<<<< HEAD
script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id is not None:
        print(x_request_id)
    else:
        print("X-Request-Id not found in the response headers.")
=======
Takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header
"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
>>>>>>> 85c830d5152b4c87b4bb23ab8ef9119fffe1b20d
