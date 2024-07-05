#!/usr/bin/python3
""" status module """
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as res:
    con = res.read()


print(f"\t- type: {type(con)}")
print(f"\t- content: {con}")
print(f"\t- utf8: {con.endcode('utf-8')}")
