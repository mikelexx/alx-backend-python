#!/usr/bin/env python3
"""
Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.
"""
import typing

def multiply(multiplier: float)->float:
    return multiplier **2

def make_multiplier(multiplier: float)->typing.Callable[[float], float]:
    """
     takes a float multiplier as argument and returns a
     function that multiplies a float by multiplier.
    """
    return multiply
