"""Unit tests for recipes.py"""

# Standard library imports
import os
import unittest
from unittest.mock import patch, mock_open

# Third party imports

# Local application imports
from context import Recipes


class TestRecipes(unittest.TestCase):
    INGREDIENTS = ['granadilla', 'tomate de arbol', 'lulo', 'maracuya', 'guanabana']
    REQUEST_URL = 'https://api.spoonacular.com/recipes/findByIngredients?ingredients=granadilla,+tomate%20de%20arbol,+lulo,+maracuya,+guanabana&number=8&limitLicense=true&ranking=1&ignorePantry=true&apiKey=[valid_api_key]'
    VALID_JSON_DATA = [{'key1': 'value1'}, {'key2': 'value2'}]
    INVALID_JSON_DATA = []
    JSON_DATA_NOT_CHNAGED = [{'data': 'did not change'}]

    def setUp(self):
        self.recipes = Recipes()


    # -------------------------------------------------------------------------
    # Tests for get_recipes
    # -------------------------------------------------------------------------
    @patch.dict(os.environ, {'SPOONACULAR_API_KEY': ''})
    def test_get_recipes_should_throw_given_api_key_not_found(self):
        with patch("builtins.open", mock_open(read_data='ABK_TEST_ENV_VAR=[invalid_api_key]')) as mock_file:
            actual_response = self.JSON_DATA_NOT_CHNAGED
            with self.assertRaises(Exception) as exception_message:
                actual_response = self.recipes.get_recipes(self.INGREDIENTS)
            self.assertEqual(str(exception_message.exception), self.recipes.API_KEY_NOT_FOUND_EXCEPTION_MESSAGE)
            mock_file.assert_called_with(self.recipes.ENVIRONMENT_FILE_NAME, 'r')
            self.assertEqual(os.environ[self.recipes.SPOONACULAR_API_KEY], '')
            self.assertEqual(actual_response, self.JSON_DATA_NOT_CHNAGED)


    @patch.dict(os.environ, {'SPOONACULAR_API_KEY': '[valid_api_key]'})
    def test_get_recipes_should_throw_given_response_not_ok_and_json_data_invalid(self):
        with patch('src.recipes.requests.get') as mock_get:
            actual_response = self.JSON_DATA_NOT_CHNAGED
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = self.INVALID_JSON_DATA
            with self.assertRaises(Exception) as exception_message:
                actual_response = self.recipes.get_recipes(self.INGREDIENTS)
            self.assertEqual(str(exception_message.exception), self.recipes.INVALID_RESPONSE_EXCEPTION_MESSAGE)
            mock_get.assert_called_with(self.REQUEST_URL)
            self.assertEqual(actual_response, self.JSON_DATA_NOT_CHNAGED)


    @patch.dict(os.environ, {'SPOONACULAR_API_KEY': '[valid_api_key]'})
    def test_get_recipes_should_throw_given_response_ok_but_json_data_invalid(self):
        with patch('src.recipes.requests.get') as mock_get:
            actual_response = self.JSON_DATA_NOT_CHNAGED
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = self.INVALID_JSON_DATA
            with self.assertRaises(Exception) as exception_message:
                actual_response = self.recipes.get_recipes(self.INGREDIENTS)
            self.assertEqual(str(exception_message.exception), self.recipes.NO_RECIPES_FOUND_PLEASE_TRY_AGAIN_EXCEPTION_MESSAGE)
            self.assertEqual(os.environ[self.recipes.SPOONACULAR_API_KEY], '[valid_api_key]')
            mock_get.assert_called_with(self.REQUEST_URL)
            self.assertEqual(actual_response, self.JSON_DATA_NOT_CHNAGED)


    @patch.dict(os.environ, {'SPOONACULAR_API_KEY': '[valid_api_key]'})
    def test_get_recipes_should_throw_given_valid_json_but_response_not_ok(self):
        with patch('src.recipes.requests.get') as mock_get:
            actual_response = self.JSON_DATA_NOT_CHNAGED
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = self.VALID_JSON_DATA
            with self.assertRaises(Exception) as exception_message:
                actual_response = self.recipes.get_recipes(self.INGREDIENTS)
            self.assertEqual(str(exception_message.exception), self.recipes.INVALID_RESPONSE_EXCEPTION_MESSAGE)
            self.assertEqual(os.environ[self.recipes.SPOONACULAR_API_KEY], '[valid_api_key]')
            mock_get.assert_called_with(self.REQUEST_URL)
            self.assertEqual(actual_response, self.JSON_DATA_NOT_CHNAGED)


    @patch.dict(os.environ, {'SPOONACULAR_API_KEY': '[valid_api_key]'})
    def test_get_recipes_should_return_valid_data_given_response_ok_and_json_data_valid(self):
        with patch('src.recipes.requests.get') as mock_get:
            actual_response = self.JSON_DATA_NOT_CHNAGED
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = self.VALID_JSON_DATA
            actual_response = self.recipes.get_recipes(self.INGREDIENTS)
            self.assertEqual(os.environ[self.recipes.SPOONACULAR_API_KEY], '[valid_api_key]')
            mock_get.assert_called_with(self.REQUEST_URL)
            self.assertEqual(actual_response, self.VALID_JSON_DATA)

    # todo: write test for ingredients which contain white spaces, the get request string should not contain white spaces


if __name__ == '__main__':
    unittest.main()
