"""Gets the price breakdown and shows final result."""

# Standard library imports

# Third party imports
from colorama import Fore, Style
import json
import requests

# Local application imports
from api_key_loader import ApiKeyLoader


class ShoppingList():
    INVALID_NUMBER_OF_RECIPES_PASSED_IN = 'No recipe selected to show in the shopping list'
    RECIPE_ID_KEY = 'id'
    SPOONACULAR_PRICE_BREAKDOWN_API_URL = 'https://api.spoonacular.com/recipes'
    SPOONACULAR_PRICE_BREAKDOWN_API_JSON = 'priceBreakdownWidget.json'
    API_KEY = 'apiKey'                  # API key is the authentication to use to run the get http request. the value must be kept secret


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
                self.__price_list.append(response.json())


    def show_final_result(self):
        pass


    def __create_request(self, id):
        api_key_value   = self.__get_api_key()
        req_api_key     = '='.join([self.API_KEY, api_key_value])
        req_url         = '/'.join([self.SPOONACULAR_PRICE_BREAKDOWN_API_URL, str(id), self.SPOONACULAR_PRICE_BREAKDOWN_API_JSON])
        request_string  = '?'.join([req_url, req_api_key])
        print(request_string)
        return request_string


    def __send_request(self, request_string):
        response = requests.get(request_string)
        self.__print_json_list(response.json())
        # print(response.text)
        return response


    def __get_api_key(self):
        if self.__api_key:
            return self.__api_key
        api_key_loader = ApiKeyLoader()
        self.__api_key = api_key_loader.get_api_key()
        return self.__api_key


    def __print_json_list(self, json_data):
        ''' This method is not tested since it used for debug info only '''
        print('----------------------------------------------------')
        print('\n'.join([json.dumps(json_data, indent=2)]))
