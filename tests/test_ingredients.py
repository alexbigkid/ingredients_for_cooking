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
        [',OneEgg,', ['OneEgg']],
        [',,TwoEggs', ['TwoEggs']],
        ['ThreeEggs,,', ['ThreeEggs']],
        [',,FourEggs,,', ['FourEggs']],
        [' , , FiveEggs , , ', ['FiveEggs']],
        ['Champignon,, banana', ['Champignon', 'banana']],
        [',, basil , , potatos,,', ['basil', 'potatos']],
    ])
    def test_read_input_should_sanitize_values(self, input, expected):
        with patch('builtins.input', return_value=input):
            actual_input = self.ingredients.read_input()
            self.assertEqual(actual_input, expected)

    @parameterized.expand([
        [''],
        [','],
        [',,'],
        [' ,  , ,'],
        ['42'],
        ['😀'],
        ['😎, 🥸'],
    ])
    def test_read_input_should_throw_exception_given_not_valid_input(self, input):
        with patch('builtins.input', return_value=input):
            with self.assertRaises(Exception) as exception_message:
                self.ingredients.read_input()
            self.assertEqual(str(exception_message.exception), self.ingredients.INVALID_INPUT_EXCEPTION_MESSAGE)

if __name__ == '__main__':
    unittest.main()
