#!/usr/bin/python3
"""add item module"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
try:
    o_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    o_list = []

o_list.extend(sys.argv[1:])
save_to_json_file(o_list, "add_item.json")
