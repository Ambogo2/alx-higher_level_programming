#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status/') as request:
        html_bytes = request.read()
        html = html_bytes.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(html_bytes))
    print("\t- content:", html_bytes)
    print("\t- utf8 content:", html)