#!/usr/bin/python3

"""Load from JSON file module"""


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        import json
        return json.load(f)
