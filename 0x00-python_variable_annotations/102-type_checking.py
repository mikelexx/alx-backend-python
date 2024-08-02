#!/usr/bin/env python3
"""
Use mypy to validate piece of code and apply any necessary changes.
"""
from typing import Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> list[Any]:
    """
    annotate this function that was given
    """
    zoomed_in: list = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
