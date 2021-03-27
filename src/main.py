import sys
from ingredients import Ingredients
from recipes import Recipes
# import colorama
from colorama import Fore, Style


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
        recipes = get_recipes(ingredient_list)
        # print results
    except Exception as exception:
        print(Fore.RED + f"ERROR: executing getting recipes with your favorite ingredients")
        print(f"{exception}{Style.RESET_ALL}")
        exit_code = 1
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
