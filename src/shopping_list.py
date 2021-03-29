"""Gets the price breakdown and shows final result."""

# Standard library imports

# Third party imports
from colorama import Fore, Style
import json
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
import requests

# Local application imports
from api_key_loader import ApiKeyLoader


class ShoppingList():
    INVALID_NUMBER_OF_RECIPES_PASSED_IN = 'No recipe selected to show in the shopping list'
    RECIPE_ID_KEY = 'id'
    RECIPE_TITTLE_KEY = 'title'
    INGREDIENT_NAME_KEY = 'name'
    INGREDIENT_PRICE_KEY = 'price'
    INGREDIENT_AISLE_NAME_KEY = 'aisle'
    MISSING_INGREDIENTS_KEY = 'missedIngredients'
    PRICE_LIST_INGREDIENT_KEY = 'ingredients'
    PRICE_LIST_TOTAL_COST_KEY = 'totalCost'
    SPOONACULAR_PRICE_BREAKDOWN_API_URL = 'https://api.spoonacular.com/recipes'
    SPOONACULAR_PRICE_BREAKDOWN_API_JSON = 'priceBreakdownWidget.json'
    API_KEY = 'apiKey'                  # API key is the authentication to use to run the get http request. the value must be kept secret
    PRETTY_TABLE_INGREDIENT = 'Missing ingredient list (well, most of them)'
    PRETTY_TABLE_AISLE = 'Aisle where to find missing ingredients in the store'
    PRETTY_TABLE_PRICE = 'Price ($)'
    ESTIMATED_COST_FOR_MISSING_INGREDIENTS_TEXT = 'Estimated cost for missing ingredients'
    ESTIMATED_COST_FOR_ALL_INGREDIENTS_TEXT = 'Estimated cost for all ingredients'
    ESTIMATED_COST_NOT_AVAILABLE_TEXT = 'Price info for this recipe is not available'


    def __init__(self, liked_recipe_list):
        # protect module from invalid input in case it is taken out of this package
        # and used somewhere else
        if not len(liked_recipe_list) > 0:
            raise Exception(self.INVALID_NUMBER_OF_RECIPES_PASSED_IN)
        self.__liked_recipe_list = liked_recipe_list
        self.__price_list = []
        self.__api_key = ''


    def get_price_breakdown(self):
        for liked_recipe in self.__liked_recipe_list:
            request_string = self.__create_request(liked_recipe[self.RECIPE_ID_KEY])
            response = self.__send_request(request_string)
            if self.__is_response_valid(response):
                response_json = response.json()
                response_json[self.RECIPE_ID_KEY] = liked_recipe[self.RECIPE_ID_KEY]
                self.__price_list.append(response_json)
            else:
                # some error happenned here, but we should not raise an exception and terminate the app
                # because the netxt recipe price request might be ok.
                # Just warning for the user that the price info for this recipe is not available
                print(Fore.YELLOW
                    + f"WARNING: Price information is unavailable for following recipe: "
                    + liked_recipe[self.RECIPE_TITTLE_KEY]
                    + f"{Style.RESET_ALL}"
                )


    def print_price_per_recipe(self):
        i = 0
        for liked_recipe in self.__liked_recipe_list:
            if liked_recipe[self.RECIPE_ID_KEY] == self.__price_list[i][self.RECIPE_ID_KEY]:
                self.__print_info_for_all_missing_ingredients_in_recipe(liked_recipe, self.__price_list[i])
                i += 1
            else:
                self.__print_price_info_not_avaibale()


    def print_final_result(self):
        pass


    def __create_request(self, id):
        api_key_value   = self.__get_api_key()
        req_api_key     = '='.join([self.API_KEY, api_key_value])
        req_url         = '/'.join([self.SPOONACULAR_PRICE_BREAKDOWN_API_URL, str(id), self.SPOONACULAR_PRICE_BREAKDOWN_API_JSON])
        request_string  = '?'.join([req_url, req_api_key])
        # print(request_string)
        return request_string


    def __send_request(self, request_string):
        response = requests.get(request_string)
        # self.__print_json_list(response.json())
        # print(response.text)
        return response


    def __get_api_key(self):
        if self.__api_key:
            return self.__api_key
        api_key_loader = ApiKeyLoader()
        self.__api_key = api_key_loader.get_api_key()
        return self.__api_key


    def __is_response_valid(self, response):
        return response.ok and response.json()


    def __print_info_for_all_missing_ingredients_in_recipe(self, recipe, price_breakdown):
        missed_ingredient_list = recipe[self.MISSING_INGREDIENTS_KEY]
        ingredient_price_list = price_breakdown[self.PRICE_LIST_INGREDIENT_KEY]
        total_missed_ingredients_price = 0.0
        pretty_table = self.__create_pretty_table_recipe_header()
        for missed_ingredient in missed_ingredient_list:
            for ingredient_price in ingredient_price_list:
                if missed_ingredient[self.INGREDIENT_NAME_KEY] == ingredient_price[self.INGREDIENT_NAME_KEY]:
                    pretty_table.add_row([
                        missed_ingredient[self.INGREDIENT_NAME_KEY],
                        missed_ingredient[self.INGREDIENT_AISLE_NAME_KEY],
                        str(ingredient_price[self.INGREDIENT_PRICE_KEY])
                    ])
                    total_missed_ingredients_price += ingredient_price[self.INGREDIENT_PRICE_KEY]
        pretty_table.add_row([self.ESTIMATED_COST_FOR_MISSING_INGREDIENTS_TEXT, '', str(round(total_missed_ingredients_price,2))])
        pretty_table.add_row([self.ESTIMATED_COST_FOR_ALL_INGREDIENTS_TEXT, '', str(price_breakdown[self.PRICE_LIST_TOTAL_COST_KEY])])
        print(pretty_table.get_string(title=recipe[self.RECIPE_TITTLE_KEY]))


    def __print_price_info_not_avaibale(self, recipe):
        pretty_table = self.__create_pretty_table_recipe_header()
        pretty_table.add_row([self.ESTIMATED_COST_NOT_AVAILABLE_TEXT, '', ''])
        print(pretty_table.get_string(title=recipe[self.RECIPE_TITTLE_KEY]))


    def __create_pretty_table_recipe_header(self):
        pretty_table = PrettyTable()
        pretty_table.set_style(MSWORD_FRIENDLY)
        pretty_table.field_names = [self.PRETTY_TABLE_INGREDIENT, self.PRETTY_TABLE_AISLE, self.PRETTY_TABLE_PRICE]
        pretty_table.align[self.PRETTY_TABLE_INGREDIENT] = 'l'
        pretty_table.align[self.PRETTY_TABLE_AISLE] = "l"
        pretty_table.align[self.PRETTY_TABLE_PRICE] = 'r'
        return pretty_table


    def __print_recipe_total_costs(self):
        pass


    def __print_json_list(self, json_data):
        ''' This method is not tested since it used for debug info only '''
        print('----------------------------------------------------')
        print('\n'.join([json.dumps(json_data, indent=2)]))
