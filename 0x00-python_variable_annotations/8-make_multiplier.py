#!/usr/bin/env python3
"""
Write a type-annotated function make_multiplier that takes a
float multiplier as argument and
returns a function that multiplies a float by multiplier.
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
     takes a float multiplier as argument and returns a
     function that multiplies a float by multiplier.
    """

    def multiply(value: float) -> float:
        """mutliplies a value by mutliplier
        supplied in the closure"""
        return multiplier * value

    return multiply
