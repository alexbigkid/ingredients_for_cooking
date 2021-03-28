"""Unit tests for recipes.py"""

# Standard library imports
import os
import unittest
from unittest.mock import patch

# Third party imports

# Local application imports
from context import ResultView


class TestResultView(unittest.TestCase):


    def setUp(self):
        self.result_view = ResultView([])


    # -------------------------------------------------------------------------
    # Tests for show_recipe_list
    # -------------------------------------------------------------------------
    def test_show_recipe_list(self):
        self.assertTrue(True)


    # -------------------------------------------------------------------------
    # Tests for show_recipe_list
    # -------------------------------------------------------------------------
    def test_show_final_result(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
