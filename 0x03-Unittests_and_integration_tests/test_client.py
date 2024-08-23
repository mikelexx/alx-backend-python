#!/usr/bin/env python3
"""
contains tests for client.py class methods
"""

import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized
from utils import get_json, access_nested_map, memoize
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    tests methods for TestGithubOrgClient class in client.py
    """

    @parameterized.expand([('google', ), ('abc', )])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json) -> None:
        """
        tests the GithubOrgClient.org method
        returns correct value
        """
        client = GithubOrgClient(org_name)
        client.org

        mock_get_json.assert_called_once_with(
            client.ORG_URL.format(org=org_name))

    @parameterized.expand([('google', ), ('abc')])
    def test_public_repos_url(self, org_name):
        """
        test public_repos_url method returns correct values
        """
        client = GithubOrgClient(org_name)
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': 'randomUrl'}
            self.assertEqual(client._public_repos_url, 'randomUrl')
