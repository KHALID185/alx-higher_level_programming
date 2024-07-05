#!/usr/bin/python3
"""
script that display the body of response
"""
from sys import argv
import urllib.request as req
import urllib.parse as parse
import urllib.error as error

if __name__ == "__main__":
    url = argv[1]

    request = req.Request(url)
    try:
        with req.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
