#!/usr/bin/env python3
"""
Contains unittests for access_nested_map function
"""
from typing import Any
import unittest
from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Implements test methods for utils module functions
    """

    @parameterized.expand([({
        "a": 1
    }, ("a", ), 1), ({
        "a": {
            "b": 2
        }
    }, ("a", ), {
        "b": 2
    }), ({
        "a": {
            "b": 2
        }
    }, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map: Any, path: Any,
                               expected_val: Any) -> None:
        """
        test access_nested_map returns proper values or raises KeyError
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_val)
        self.assertRaises(KeyError, access_nested_map, 'invalidmap', 'b')
