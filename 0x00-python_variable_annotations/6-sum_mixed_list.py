#!/usr/bin/env python3
"""
contains a type-annotated function sum_list which takes a
list input_list of floats as argument and
returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """
    takes a list mxd_lst of integers and floats and returns
    their sum as a float.
    """
    x = 0.0
    for val in mxd_lst:
        x += val
    return x
