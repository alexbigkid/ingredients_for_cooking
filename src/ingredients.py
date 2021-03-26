class Ingredients():
    USER_PROMPT_FOR_INGREDIENTS = 'Please enter your favorite ingredients separated by comma:'

    def ask_for_ingredients(self):
        print(self.USER_PROMPT_FOR_INGREDIENTS)

    def read_input(self):
        ingredients = input()
        ingredients = ingredients.split(',')
        ingredients = self.__sanitize_input(ingredients)
        if self.__is_input_valid(ingredients):
            return ingredients
        else:
            raise Exception("ERROR: Ivalid input. Please use only alpha-numeric characters and white spaces.")

    def __sanitize_input(self, ingredient_list):
        ingredients = [ingredient.strip(' ') for ingredient in ingredient_list]
        return list(filter(None, ingredients))

    def __is_input_valid(self, ingredient_list):
        return len(ingredient_list) != 0 and \
            all(ingredient.replace(' ','').isalnum() for ingredient in ingredient_list)

