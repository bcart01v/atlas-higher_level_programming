#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    first_sum = tuple_a[0] + tuple_b[0]
    second_sum = tuple_a[1] + tuple_b[1]

    return (first_sum, second_sum)
