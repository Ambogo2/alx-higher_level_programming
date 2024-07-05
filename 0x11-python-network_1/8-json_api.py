#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL """

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    data = {'q': letter}
    # post request
    response = requests.post(url, data=data)

    try:
        # parse response as JSON
        parsed_response = response.json()

        if parsed_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(parsed_response.get("id"),
                                    parsed_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
