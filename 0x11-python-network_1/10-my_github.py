#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL """

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.arv[2]

    url = 'https://api.github.com/user'

    # authentication
    auth = HTTPBasicAuth(username, password)

    # send get request to github api
    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
