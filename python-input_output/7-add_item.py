#!/usr/bin/python3
'''Module 7-add_item'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


JSON_list = []

try:
    JSON_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass

for arg in range(1, len(sys.argv)):
    JSON_list.append(sys.argv[arg])
save_to_json_file(JSON_list, "add_item.json")
