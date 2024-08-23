#!/usr/bin/env python3
"""
Contains unittests for access_nested_map function
"""
from typing import Any, Callable
import unittest
import requests
from parameterized import parameterized
from unittest.mock import Mock, _patch, patch

get_json = __import__('utils').get_json
access_nested_map = __import__('utils').access_nested_map
memoize = __import__('utils').memoize


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

    @parameterized.expand([({}, ("a", ), 'a'), ({"a": 1}, ("a", "b"), 'b')])
    def test_access_nested_map_exception(self, nested_map: Any, path: Any,
                                         expected_val: Any) -> None:
        """
        test KeyError is raised for accessing invalid nested_map
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception), f"'{expected_val}'")


class TestGetJson(unittest.TestCase):
    """
    test mocking http/function calls and their returns
    """

    @parameterized.expand([("http://example.com", {
        "payload": True
    }), ("http://holberton.io", {
        "payload": False
    })])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get) -> None:
        """
        testing that mock function replaces an exensice http call function in
        get_json function
        """
        mock_response = Mock()

        mock_response.json.return_value = test_payload
        mock_requests_get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    implements tests for memoizing functions
    """

    def test_memoize(self) -> None:
        """
        Tests the memoize decorator caches the results of function
        """

        class TestClass:
            """
            simple class with which to test memoization with its attributes
            """

            def a_method(self):
                """
                simple function to simulate expensive function
                """
                return 42

            @memoize
            def a_property(self):
                """
                memoized result of a_method to be acessed as property
                """
                return self.a_method()

        inst = TestClass()
        with patch.object(inst, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            self.assertEqual(inst.a_property, 42)
            self.assertEqual(inst.a_property, 42)
            mock_a_method.assert_called_once()
