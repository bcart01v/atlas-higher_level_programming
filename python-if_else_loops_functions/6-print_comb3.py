#!/usr/bin/python3

for i in range(8):
    for j in range(i + 1, 10):
        if i < 8 or (i == 8 and j < 9):
            print("{:02d}, ".format(i * 10 + j), end="")
        else:
            print("{:02d}".format(i * 10 + j), end="\n")
