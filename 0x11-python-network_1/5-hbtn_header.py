#!/usr/bin/python3
"""Script that fetches X-Request-Id header from a specified URL"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    res = r.headers.get('X-Request-Id')
    print(res)
