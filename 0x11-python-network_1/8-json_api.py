#!/usr/bin/python3
"""send a post request with letter"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    param = {'q': q}
    res = requests.post(url, params=param)
    try:
        json_data = res.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
