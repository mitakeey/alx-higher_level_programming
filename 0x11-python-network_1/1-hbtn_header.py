#!/usr/bin/python3
"""
 Gets URL and sends a request to the URL
 displays the value of the variable in the header ofthe response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
