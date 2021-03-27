"""Main program for displaying ingredients list for shopping with the recipes liked"""

# Standard library imports
import sys

# Third party imports
from colorama import Fore, Style

# Local application imports
from .ingredients import Ingredients
from .recipes import Recipes


def get_ingredients():
    ingredients = Ingredients()
    ingredients.ask_for_ingredients()
    return ingredients.read_input()


def get_recipes(ingredients):
    recipes = Recipes()
    return recipes.get_recipes(ingredients)


def main():
    exit_code = 0
    try:
        # ingredient_list = get_ingredients()
        # print('You entered: ' + ', '.join(ingredient_list))
        # ingredient_list = ['apple', 'venigar', 'oil']
        ingredient_list = ['apple', 'sugar']
        recipe_list = get_recipes(ingredient_list)
        # print results
    except Exception as exception:
        print(Fore.RED + f"ERROR: executing getting recipes with your favorite ingredients")
        print(f"{exception}{Style.RESET_ALL}")
        exit_code = 1
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
