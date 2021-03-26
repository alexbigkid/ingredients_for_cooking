import sys
from ingredients import Ingredients
# import colorama
from colorama import Fore, Style


def get_ingredients():
    ingredients = Ingredients()
    ingredients.ask_for_ingredients()
    return ingredients.read_input()

def main():
    exit_code = 0
    try:
        ingredients_array = get_ingredients()
        print('You entered: ' + ', '.join(ingredients_array))
        # get recepies
        # print results
    except Exception as exception:
        print(Fore.RED + f"ERROR: executing getting recipe with your favorite ingredients")
        print(f"{exception}{Style.RESET_ALL}")
        exit_code = 1
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
