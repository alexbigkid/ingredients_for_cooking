"""Main program for displaying ingredients list for shopping with the recipes liked"""

# Standard library imports
import sys

# Third party imports
from colorama import Fore, Style

# Local application imports
from ingredients import Ingredients
from recipes import Recipes
from result_view import ResultView


def get_ingredients():
    ingredients = Ingredients()
    ingredients.ask_for_ingredients()
    return ingredients.read_input()


def get_recipes(ingredients):
    recipes = Recipes()
    return recipes.get_recipes(ingredients)


def show_results(recipes):
    result = ResultView(recipes)
    result.show_recipe_list()
    result.show_final_result()


def main():
    exit_code = 0
    try:
        # ingredient_list = get_ingredients()
        # ingredient_list = ['apple', 'venigar', 'oil']
        # ingredient_list = ['granny smith apples', 'sugar', 'venigar']
        ingredient_list = ['garlic', 'ginger', 'granny smith apple']
        recipe_list = get_recipes(ingredient_list)
        show_results(recipe_list)
    except Exception as exception:
        print(Fore.RED + f"ERROR: executing getting recipes with your favorite ingredients")
        print(f"{exception}{Style.RESET_ALL}")
        exit_code = 1
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
