#!/usr/bin/python3
"""File I/O"""
import json
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
from sys import argv


mylist = []
for x in range(1, len(argv)):
    mylist.append(argv[x])
try:
    exsistingList = load_from_json_file("add_item.json")
except Exception:
    pass
else:
    mylist = exsistingList + mylist
save_to_json_file(mylist, "add_item.json")
