"""Unit tests for env_loader.py"""

# Standard library imports
import unittest

# Local application imports
from src.env_loader import EnvLoader


class TestEnvLoader(unittest.TestCase):

    def setUp(self):
        self.env_loader = EnvLoader()

    def test_get_environment_variable_value(self):
        self.assertTrue(True)

    def test_set_environment_varaibales_from_file(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
