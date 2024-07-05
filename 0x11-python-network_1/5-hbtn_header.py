#!/usr/bin/python3
"""
script that take a url and send a request 
and displays variable X-Request-ID
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
