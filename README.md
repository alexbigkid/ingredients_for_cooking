# Ingredients for coocking
Creates a shopping list with your favorite ingredients for recipes you liked.

## APY KEY note
To be able to execute this python program an API KEY for the Spoonacular
http service is required. Since it is sensitive information and should
not be added to the plain view of source code, you would need to set up
an environment variable in you terminal with following command:<br>
export SPOONACULAR_API_KEY=<spoonacular_api_key_here>

Or alternatively you can create file .env in root directory of this project
and add following line into the .env file:<br>
SPOONACULAR_API_KEY=<spoonacular_api_key_here>


## Instructions for users
| make rule    | description                         |
| ------------ | ----------------------------------- |
| make install | installs needed python dependencies |
| make my_dish | starts the program                  |


## Instructions for developers
| make rule         | description                                  |
| ----------------- | -------------------------------------------- |
| make help         | to see all make rules                        |
| make my_dish      | executes the main program                    |
| make install      | installs required packages                   |
| make install_dev  | installs required development packages       |
| make test         | runs test                                    |
| make test_verbose | runs test with verbose messaging             |
| make coverage     | runs test, produces coverage and displays it |


## Notes for reviewers
Since I was not very familar with unittest frame work (I used pytest in the past)
I experemented with different way writing tests: using mocks, patches and DIs
That should be considered a unittest practice and not a bad testing design.
Usually I write code with one style for better readability.


## API used
### this project utilizes Spoonacular API to get recipes from ingredient list
[Spoonacular API](https://spoonacular.com/food-api/docs)

### To get the recipes from the list of ingredients following API is used
[Get recipes from ingredients API](https://spoonacular.com/food-api/docs#Search-Recipes-by-Ingredients)
