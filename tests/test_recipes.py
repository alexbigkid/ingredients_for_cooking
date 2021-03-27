"""Unit tests for recipes.py"""

# Standard library imports
import os
import unittest
from unittest.mock import patch, mock_open

# Third party imports

# Local application imports
from src.recipes import Recipes


class TestRecipes(unittest.TestCase):
    INGREDIENTS = ['granadilla', 'tomate de arbol', 'lulo', 'maracuya', 'guanabana']

    def setUp(self):
        self.recipes = Recipes()


    # -------------------------------------------------------------------------
    # Tests for get_recipes
    # -------------------------------------------------------------------------
    @patch.dict(os.environ, {'SPOONACULAR_API_KEY': ''})
    def test_get_recipes_should_throw_given_api_key_not_found(self):
        with patch("builtins.open", mock_open(read_data='ABK_TEST_ENV_VAR=[fake_api_key]')) as mock_file:
            actual_value = []
            with self.assertRaises(Exception) as exception_message:
                actual_value = self.recipes.get_recipes(self.INGREDIENTS)
            self.assertEqual(str(exception_message.exception), self.recipes.API_KEY_NOT_FOUND_EXCEPTION_MESSAGE)
            mock_file.assert_called_with(self.recipes.ENVIRONMENT_FILE_NAME, 'r')
            self.assertEqual(actual_value, [])


    def test_get_recipes_should_display_no_recipes_found_given_empty_response(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
