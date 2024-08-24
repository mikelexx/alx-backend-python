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
    def test_public_repos_url(self, org_name) -> None:
        """
        test public_repos_url method returns correct values
        """
        client = GithubOrgClient(org_name)
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': 'randomUrl'}
            self.assertEqual(client._public_repos_url, 'randomUrl')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json) -> None:
        """
        unit-testing GithubOrgClient.public_repos
        """
        mock_get_json.return_value = [{
            'name': 'libcxx',
            'license': {
                'key': 'MIT'
            }
        }, {
            'name': 'CSP-Validator',
            'license': {
                'expire': '2026'
            }
        }, {
            'name': 'autoparse'
        }]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'urlforgoogle'
            client = GithubOrgClient('google')
            self.assertEqual(client.public_repos(),
                             ['libcxx', 'CSP-Validator', 'autoparse'])
            self.assertEqual(client.public_repos('MIT'), ['libcxx'])
            mock_get_json.assert_called_once_with('urlforgoogle')
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license_key, expected_val):
        """
        unit-test GithubOrgClient.has_license method
        """
        self.assertIs(GithubOrgClient.has_license(repo, license_key), expected_val)
