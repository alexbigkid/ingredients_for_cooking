"""Sends request using spoonacular API and evaluates the response with recipes"""

# Standard library imports
import requests
import json

# Local application imports
from .env_loader import EnvLoader

class Recipes():
    SPOONACULAR_API_URL = 'https://api.spoonacular.com/recipes/findByIngredients'
    INGREDIENTS_KEY = 'ingredients'     # A comma-separated list of ingredients that the recipes should contain.
    NUMBER_KEY = 'number'               # The maximum number of recipes to return (between 1 and 100). Defaults to 10.
    NUMBER_VALUE = '8'
    LIMIT_LICENSE_KEY = 'limitLicense'  # Whether the recipes should have an open license that allows display with proper attribution.
    LIMIT_LICENSE_VALUE = 'true'
    RANKING_KEY = 'ranking'             # Whether to maximize used ingredients (1) or minimize missing ingredients (2) first.
    RANKING_VALUE = '1'
    IGNORE_PANTRY_KEY = 'ignorePantry'  # Whether to ignore typical pantry items, such as water, salt, flour, etc.
    IGNORE_PANTRY_VALUE = 'true'
    API_KEY = 'apiKey'                  # API key is the authentication to use to run the get http request. the value must be kept secret
    SPOONACULAR_API_KEY = 'SPOONACULAR_API_KEY'
    ENVIRONMENT_FILE_NAME = '.env'
    INVALID_RESPONSE_EXCEPTION_MESSAGE = 'EXCEPTION: Invalid response received.'

    API_KEY_NOT_FOUND_EXCEPTION_MESSAGE = 'EXCEPTION: spoonacular API key could not be found. Please load env variable SPOONACULAR_API_KEY with api key or set it in the .env file.'


    def get_recipes(self, ingredient_list):
        print('ingredients: ' + ', '.join([ingredient for ingredient in ingredient_list]))
        request_string = self.__create_request(ingredient_list)
        response = self.__send_request(request_string)
        # self.__print_response(response)
        if self.__is_response_valid(response):
            return response.json()
        else:
            raise Exception(self.INVALID_RESPONSE)

    def __create_request(self, ingredient_list):
        api_key_value       = self.__get_api_key()
        ingredients         = ',+'.join([ingredient for ingredient in ingredient_list])
        req_ingredients     = '='.join([self.INGREDIENTS_KEY, ingredients])
        req_number          = '='.join([self.NUMBER_KEY, self.NUMBER_VALUE])
        req_limit_license   = '='.join([self.LIMIT_LICENSE_KEY, self.LIMIT_LICENSE_VALUE])
        req_ranking         = '='.join([self.RANKING_KEY, self.RANKING_VALUE])
        req_ignore_pantry   = '='.join([self.IGNORE_PANTRY_KEY, self.IGNORE_PANTRY_VALUE])
        req_api_key         = '='.join([self.API_KEY, api_key_value])
        req_parameters      = '&'.join([req_ingredients, req_number, req_limit_license, req_ranking, req_ignore_pantry, req_api_key])
        request_string      = '?'.join([self.SPOONACULAR_API_URL, req_parameters])
        # print(request_string)
        return request_string

    def __get_api_key(self):
        env_loader = EnvLoader()
        spoonacular_api_key = env_loader.get_api_key_from_environment_variable(self.SPOONACULAR_API_KEY)
        if not spoonacular_api_key:
            env_loader.set_environment_varaibales_from_file(self.ENVIRONMENT_FILE_NAME)
            spoonacular_api_key = env_loader.get_api_key_from_environment_variable(self.SPOONACULAR_API_KEY)
            if not spoonacular_api_key:
                raise Exception(self.INVALID_INPUT_EXCEPTION_MESSAGE)
        return spoonacular_api_key

    def __send_request(self, request_string):
        response = requests.get(request_string)
        # print('status code: ' + str(response.status_code))
        # print('response_text: ' + response.text)
        # print('\n')
        response_json = response.json()
        self.__print_json_list(response_json)
        return response

    def __is_response_valid(self, response):
        return True

    def __print_response(self, response):
        pass

    def __print_json_list(self, json_list):
        ''' This method is not tested since it used for debug info only '''
        json_list_length = len(json_list)
        if json_list_length > 0:
            print(': '.join(['json_list_length', str(json_list_length)]))
            print('----------------------------------------------------')
            print('\n'.join([json.dumps(i_recipe, indent=2) for i_recipe in json_list]))
