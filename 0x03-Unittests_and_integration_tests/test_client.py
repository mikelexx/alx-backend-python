#!/usr/bin/env python3
"""
contains tests for client.py class methods
"""

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import get_json, access_nested_map, memoize
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    tests methods for TestGithubOrgClient class in client.py
    """

    @parameterized.expand([('google', ), ('abc', )])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        tests the GithubOrgClient.org method
        returns correct value
        """
        client = GithubOrgClient(org_name)
        client.org

        mock_get_json.assert_called_once_with(
            client.ORG_URL.format(org=org_name))
