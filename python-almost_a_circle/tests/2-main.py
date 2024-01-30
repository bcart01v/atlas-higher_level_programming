#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":


    try:
        r = Rectangle(1, -13)
    except Exception as e:
        print("[2{}] {}".format(e.__class__.__name__, e))

