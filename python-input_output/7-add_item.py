#!/usr/bin/python3
"""Load, add, save"""
import sys
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    try:
        list = load_from_json_file(filename)
    except FileNotFoundError:
        list = []
    list.extend(sys.argv[1:])
    save_to_json_file(list, filename)
