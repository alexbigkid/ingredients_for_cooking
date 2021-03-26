class Ingredients():
    USER_PROMPT_FOR_INGREDIENTS = 'Please enter your favorite ingredients separated by comma: '

    def __init__(self):
        self.__ingredient_list = None

    def ask_for_ingredients(self):
        print(self.USER_PROMPT_FOR_INGREDIENTS)

    def read_input(self):
        user_input = input()
        # if __is_input_valid(user_input):
        ingredients = user_input.split(',')
        return [ingredient.strip(' ') for ingredient in ingredients]

    @property
    def user_list(self): return self.__ingredient_list
