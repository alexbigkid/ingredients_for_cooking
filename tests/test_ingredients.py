import unittest
from io import StringIO
from unittest.mock import patch
from parameterized import parameterized

from src.ingredients import Ingredients


class TestIngredients(unittest.TestCase):

    def setUp(self):
        self.ingredients = Ingredients()

    def test_ask_for_ingredients_prompts_user_to_enter_ingredients(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.ingredients.ask_for_ingredients()
            actual_stdout = fakeOutput.getvalue().rstrip('\n')
            self.assertEqual(
                actual_stdout, self.ingredients.USER_PROMPT_FOR_INGREDIENTS)

    @parameterized.expand([
        ['eggs', ['eggs']],
        ['Champignon, green apple', ['Champignon', 'green apple']],
        ['green onion, red potatos', ['green onion', 'red potatos']],
        ['green onion, red potatos, sweet potato, dark chocolate',
            ['green onion', 'red potatos', 'sweet potato', 'dark chocolate']],
    ])
    def test_read_input_with_valid_values(self, input, expected):
        with patch('builtins.input', return_value=input):
            actual_input = self.ingredients.read_input()
            self.assertEqual(actual_input, expected)

    @parameterized.expand([
        [',eggs1,', ['eggs1']],
        [',,eggs2', ['eggs2']],
        ['eggs3,,', ['eggs3']],
        [',,eggs4,,', ['eggs4']],
        [' , , eggs5 , , ', ['eggs5']],
        ['Champignon,, banana', ['Champignon', 'banana']],
        [',, basil , , potatos,,', ['basil', 'potatos']],
    ])
    def test_read_input_should_sanitize_values(self, input, expected):
        with patch('builtins.input', return_value=input):
            actual_input = self.ingredients.read_input()
            self.assertEqual(actual_input, expected)

    @parameterized.expand([
        ['', 'ERROR: Not valid input. Please use alpha-numeric characters.'],
        [',', 'ERROR: Not valid input. Please use alpha-numeric characters.'],
        [',,', 'ERROR: Not valid input. Please use alpha-numeric characters.'],
        [' ,      , ,', 'ERROR: Not valid input. Please use alpha-numeric characters.'],
        ['😀', 'ERROR: Not valid input. Please use alpha-numeric characters.'],
        ['😎, 🥸', 'ERROR: Not valid input. Please use alpha-numeric characters.'],
    ])
    def test_read_input_should_throw_exception_given_not_valid_input(self, input, expected_exception):
        with patch('builtins.input', return_value=input):
            with self.assertRaises(Exception):
                self.ingredients.read_input()


if __name__ == '__main__':
    unittest.main()
