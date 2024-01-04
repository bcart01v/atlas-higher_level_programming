#!/usr/bin/python3
from sys import argv

def main():
    total_args = len(argv) - 1
    arg_label = "argument" if total_args == 1 else "arguments"
    end_symbol = "." if total_args == 0 else ":"

    print(f"{total_args} {arg_label}{end_symbol}")

    for position in range(1, len(argv)):
        print(f"{position}: {argv[position]}")

if __name__ == "__main__":
    main()
