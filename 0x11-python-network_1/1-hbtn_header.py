#!/usr/bin/python3
"""
script that sends a request to the URL
and displays the value of the X-Request-Id
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
