import requests
import json

apikey = ''

print('What Ingredients do you currently have?')
ingredients = input()
ingredients = ingredients.replace(' ', '+')

recipe_results = requests.get(f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={apikey}&ingredients={ingredients}&number=10')


def print_results(a):
    print(json.dumps(recipe_results.json()[a]['title'], indent=4))

print_results(0)

print_results(1)

print_results(2)

print_results(3)

print_results(4)

print_results(5)

print_results(6)