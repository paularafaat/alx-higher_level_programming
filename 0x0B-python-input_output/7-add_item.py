#!/usr/bin/python3
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
import sys


try:
    n_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    n_list = []

n_list.extend(sys.argv[1:])
save_to_json_file(n_list, "add_item.json")
