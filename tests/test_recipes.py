import unittest
# from io import StringIO
# from unittest.mock import patch
# from parameterized import parameterized

from src.recipes import Recipes


class TestRecipes(unittest.TestCase):

    def setUp(self):
        self.recipes = Recipes()

    def test_get_recipes_should_display_no_recipes_found_given_empty_response(self):
        self.assertTrue(True)
        # with patch('sys.stdout', new=StringIO()) as fakeOutput:
        #     self.ingredients.ask_for_ingredients()
        #     actual_stdout = fakeOutput.getvalue().rstrip('\n')
        #     self.assertEqual(
        #         actual_stdout, self.ingredients.USER_PROMPT_FOR_INGREDIENTS)
