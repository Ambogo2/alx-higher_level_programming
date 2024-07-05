#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request"""

import urllib.request
from urllib import parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    data_encoded = parse.urlencode(data).encode('ascii')

    # making a post request
    with urllib.request.urlopen(url, data=data_encoded) as response:
        # reading and decoding response body
        print(response.read().decode('utf-8'))
