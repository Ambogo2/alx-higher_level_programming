#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # dictionary with email parameter
    data = {'email': email}

    response = requests.post(url, data)

    print(response.text)
