""" Unit tests for recipes.py """

# Standard library imports
import unittest

# Third party imports

# Local application imports
from src.recipes import Recipes


class TestRecipes(unittest.TestCase):

    def setUp(self):
        self.recipes = Recipes()

    def test_get_recipes_should_display_no_recipes_found_given_empty_response(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
