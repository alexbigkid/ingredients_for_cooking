"""
Shows user recipes. User is prompted to select recipes to his/her liking.
The summery of the shopping cart will be displayed on the end
"""

class ResultView():


    def __init__(self, recipe_list):
        self.recipe_list = recipe_list
        self.recipe_liked_list = []


    def show_recipe_list(self, recipe):
        pass


    def show_final_result(self, recipe):
        pass


    def __show_recipe(self, recipe):
        pass


    def __ask_user_selection(self, recipe):
        pass





    # def __sanitize_input(self, ingredient_list):
    #     ingredients = [ingredient.strip(' ') for ingredient in ingredient_list]
    #     return list(filter(None, ingredients))


    # def __is_input_valid(self, ingredient_list):
    #     return len(ingredient_list) != 0 and \
    #         all(ingredient.replace(' ','').isalpha() for ingredient in ingredient_list)
