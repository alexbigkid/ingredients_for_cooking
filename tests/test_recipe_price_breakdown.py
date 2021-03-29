"""Unit tests for recipe_price_breakdown.py"""

# Standard library imports
import os
from io import StringIO
import unittest
from unittest.mock import patch

# Third party imports
from colorama import Fore, Style

# Local application imports
from context import RecipePriceBreakdown


class TestRecipePriceBreakdown(unittest.TestCase):
    TEST_DATA = [{"id":647615,"title":"Huli-Huli Chicken","image":"https://spoonacular.com/recipeImages/647615-312x231.jpg","imageType":"jpg","usedIngredientCount":2,"missedIngredientCount":2,"missedIngredients":[{"id":1005006,"amount":6.0,"unit":"","unitLong":"","unitShort":"","aisle":"Meat","name":"chicken drumsticks and thighs","original":"6 CHICKEN DRUMSTICKS AND 4 THIGHS","originalString":"6 CHICKEN DRUMSTICKS AND 4 THIGHS","originalName":"CHICKEN DRUMSTICKS AND 4 THIGHS","metaInformation":[],"meta":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/chicken-parts.jpg"},{"id":9266,"amount":8.0,"unit":"ounces","unitLong":"ounces","unitShort":"oz","aisle":"Produce","name":"pineapple","original":"8 ounces crushed pineapple, undrained","originalString":"8 ounces crushed pineapple, undrained","originalName":"crushed pineapple, undrained","metaInformation":["crushed","undrained"],"meta":["crushed","undrained"],"image":"https://spoonacular.com/cdn/ingredients_100x100/pineapple.jpg"}],"usedIngredients":[{"id":11215,"amount":4.0,"unit":"","unitLong":"","unitShort":"","aisle":"Produce","name":"garlic cloves","original":"4 CLOVES GARLIC -SMASHED","originalString":"4 CLOVES GARLIC -SMASHED","originalName":"CLOVES GARLIC -SMASHED","metaInformation":[],"meta":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/garlic.png"},{"id":11216,"amount":4.0,"unit":"","unitLong":"","unitShort":"","aisle":"Produce;Ethnic Foods;Spices and Seasonings","name":"ginger root","original":"4 SLICES GINGER ROOT-SMASHED","originalString":"4 SLICES GINGER ROOT-SMASHED","originalName":"SLICES GINGER ROOT-SMASHED","metaInformation":[],"meta":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/ginger.png"}],"unusedIngredients":[{"id":1089003,"amount":1.0,"unit":"serving","unitLong":"serving","unitShort":"serving","aisle":"Produce","name":"granny smith apple","original":"granny smith apple","originalString":"granny smith apple","originalName":"granny smith apple","metaInformation":[],"meta":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/grannysmith-apple.png"}],"likes":2}]
    REQUEST_URL = 'https://api.spoonacular.com/recipes/647615/priceBreakdownWidget.json?apiKey=[valid_api_key]'
    VALID_JSON_DATA = {'key1': 'value1'}
    INVALID_JSON_DATA = {}
    JSON_DATA_NOT_CHANGED = {'data': 'did not change'}
    EXPECTED_WARNING_PRINT = "WARNING: Price information is unavailable for following recipe: Huli-Huli Chicken"

    def setUp(self):
        self.__recipe_price_breakdown = RecipePriceBreakdown(self.TEST_DATA)


    # -------------------------------------------------------------------------
    # Tests for get_price_breakdown
    # -------------------------------------------------------------------------
    @patch.dict(os.environ, {'SPOONACULAR_API_KEY': '[valid_api_key]'})
    def test_get_price_breakdown_should_print_warning_given_response_ok_is_false_and_json_data_invalid(self):
        """
            get_price_breakdown method should print a warning message
            given return value from API ok == false and json data is invalid
        """
        with patch('src.recipe_price_breakdown.requests.get') as mock_get:
            actual_response = self.JSON_DATA_NOT_CHANGED
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = self.INVALID_JSON_DATA

            with patch('sys.stdout', new=StringIO()) as fakeOutput:
                actual_price_list = self.__recipe_price_breakdown.get_price_breakdown()
                actual_stdout = fakeOutput.getvalue()
                self.assertTrue(self.EXPECTED_WARNING_PRINT in actual_stdout)
                self.assertEqual(actual_price_list, [])


    @patch.dict(os.environ, {'SPOONACULAR_API_KEY': '[valid_api_key]'})
    def test_get_price_breakdown_should_print_warning_given_response_ok_is_true_and_json_data_invalid(self):
        """
            get_price_breakdown method should print a warning message
            given return value from API ok == true and json data is invalid
        """
        with patch('src.recipe_price_breakdown.requests.get') as mock_get:
            actual_response = self.JSON_DATA_NOT_CHANGED
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = self.INVALID_JSON_DATA

            with patch('sys.stdout', new=StringIO()) as fakeOutput:
                actual_price_list = self.__recipe_price_breakdown.get_price_breakdown()
                actual_stdout = fakeOutput.getvalue()
                self.assertTrue(self.EXPECTED_WARNING_PRINT in actual_stdout)
                self.assertEqual(actual_price_list, [])


    @patch.dict(os.environ, {'SPOONACULAR_API_KEY': '[valid_api_key]'})
    def test_get_price_breakdown_should_print_warning_given_response_ok_is_false_and_json_data_valid(self):
        """
            get_price_breakdown method should print a warning message
            given return value from API ok == false and json data is valid
        """
        with patch('src.recipe_price_breakdown.requests.get') as mock_get:
            actual_response = self.JSON_DATA_NOT_CHANGED
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = self.VALID_JSON_DATA

            with patch('sys.stdout', new=StringIO()) as fakeOutput:
                actual_price_list = self.__recipe_price_breakdown.get_price_breakdown()
                actual_stdout = fakeOutput.getvalue()
                self.assertTrue(self.EXPECTED_WARNING_PRINT in actual_stdout)
                self.assertEqual(actual_price_list, [])


    @patch.dict(os.environ, {'SPOONACULAR_API_KEY': '[valid_api_key]'})
    def test_get_price_breakdown_should_print_warning_given_response_ok_is_true_and_json_data_valid(self):
        """
            get_price_breakdown method should print a warning message
            given return value from API ok == true and json data is valid
        """
        expected_price = self.VALID_JSON_DATA
        expected_price['id'] = self.TEST_DATA[0]['id']
        with patch('src.recipe_price_breakdown.requests.get') as mock_get:
            actual_response = self.JSON_DATA_NOT_CHANGED
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = self.VALID_JSON_DATA

            actual_price_list = self.__recipe_price_breakdown.get_price_breakdown()
            mock_get.assert_called_with(self.REQUEST_URL)
            self.assertEqual(actual_price_list, [expected_price])


if __name__ == '__main__':
    unittest.main()
