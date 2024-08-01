#!/usr/bin/env python3
"""
contains a type-annotated function sum_list
which takes a list input_list of floats as argument and
returns their sum as a float.
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    takes a list input_list of floats as argument and
    returns their sum as a float.
    """
    total: float = 0.0
    for el in input_list:
        total += el
    return total
