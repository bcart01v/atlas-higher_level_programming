#!/usr/bin/python3

"""Save Object to a file module"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""

    with open(filename, mode="w", encoding="utf-8") as f:
        import json
        f.write(json.dumps(my_obj))
