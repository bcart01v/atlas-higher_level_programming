#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    add_total = add(a, b)
    sub_total = sub(a, b)
    mul_total = mul(a, b)
    div_total = div(a, b)

    print("{} + {} = {}".format(a, b, add_total))
    print("{} - {} = {}".format(a, b, sub_total))
    print("{} * {} = {}".format(a, b, mul_total))
    print("{} / {} = {}".format(a, b, div_total))