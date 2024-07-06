#!/usr/bin/python3
"""Send a GET request to a URL and display the response body"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            print(data)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
