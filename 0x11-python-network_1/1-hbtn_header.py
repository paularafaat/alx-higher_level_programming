#!/usr/bin/python3
""" header module """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        x_request_id = res.getheader('X-Request-Id')
        print(x_request_id)
