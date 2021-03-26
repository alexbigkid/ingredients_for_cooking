import unittest
from io import StringIO
from unittest.mock import patch
from parameterized import parameterized

from src.ingredients import Ingredients


class TestIngredients(unittest.TestCase):

    def setUp(self):
        self.ingredients = Ingredients()

    def test_ingredients_instanciates_with_empty_ingredients_list(self):
        self.assertIsNone(self.ingredients.user_list)

    def test_ask_for_ingredients_prompts_user_to_enter_ingredients(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.ingredients.ask_for_ingredients()
            actual_stdout = fakeOutput.getvalue().rstrip('\n')
            self.assertEqual(
                actual_stdout, self.ingredients.USER_PROMPT_FOR_INGREDIENTS)

    @parameterized.expand([
        ['eggs', ['eggs']],
        ['champions, green apple', ['champions', 'green apple']],
        ['green onion, red potatos', ['green onion', 'red potatos']],
        ['green onion, red potatos, sweet potato, dark chocolate',
            ['green onion', 'red potatos', 'sweet potato', 'dark chocolate']],
    ])
    def test_read_users_input_with_valid_values(self, input, expected):
        with patch('builtins.input', return_value=input):
            actual_input = self.ingredients.read_input()
            self.assertEqual(actual_input, expected)

if __name__ == '__main__':
    unittest.main()
