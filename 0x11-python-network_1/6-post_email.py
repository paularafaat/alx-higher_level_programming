#!/usr/bin/python3
"""Send a POST request with an email as a parameter and display the response"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
