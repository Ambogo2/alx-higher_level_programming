#!/usr/bin/python3
""" takes in a URL, sends a request to the URL"""

from urllib import error, request
import sys

if __name__ == "__main__":
    # Get the URL from the command line
    url = sys.argv[1]

    try:
        # Make a GET request to the URL
        with request.urlopen(url) as response:
            # Read and decode the response body
            print(response.read().decode('utf-8'))

    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
