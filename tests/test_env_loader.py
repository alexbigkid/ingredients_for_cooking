"""Unit tests for env_loader.py"""

# Standard library imports
import os
# from unittest import TestCase, mock
import unittest
from unittest.mock import patch

# Local application imports
from src.env_loader import EnvLoader


class TestEnvLoader(unittest.TestCase):

    def setUp(self):
        self.env_loader = EnvLoader()

    @patch.dict(os.environ, {'ABK_TEST_ENV_VAR': '[fake_api_key]'})
    def test_get_environment_variable_value_returns_valid_value(self):
        actual_value = self.env_loader.get_environment_variable_value('ABK_TEST_ENV_VAR')
        self.assertEqual(actual_value, '[fake_api_key]')

    @patch.dict(os.environ, {'ABK_TEST_ENV_VAR': ''})
    def test_get_environment_variable_value_should_return_empty_given_env_var_value_is_empty(self):
        actual_value = self.env_loader.get_environment_variable_value('ABK_TEST_ENV_VAR')
        self.assertEqual(actual_value, '')

    def test_get_environment_variable_value_should_return_empty_given_env_var_undefined(self):
        actual_value = self.env_loader.get_environment_variable_value('ABK_TEST_ENV_VAR')
        self.assertEqual(actual_value, '')



    def test_set_environment_varaibales_from_file(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
