import json
import os

# TODO:
# - Organize shopping list by type
# - Seed week with one recipe, then pick other recipes with shared ingredients
# - Pick recipes instead of making list from entire directory
# - Randomize X number of recipes from recipe directory
# - If an ingredient only has one unit of something, use singular description

shopping_dict = {}

def lbs_to_ounces(lbs):
    return lbs * 16

def ounces_to_lbs(ounces):
    return ounces / 16

def parse_ingredient(ingredient):
    quantity = ingredient['quantity']
    unit = ingredient['unit']
    name = ingredient['name']
    type = ingredient['type']

    #print("Parsing ingredient " + name)
    if ingredient['name'] in shopping_dict:
        shopping_dict[name]['quantity'] += quantity
    else:
        shopping_dict[name] = { 'quantity': quantity, 'unit': unit }

def parse_recipe(recipe):
    for ingredient in recipe['ingredients']:
        parse_ingredient(ingredient)

def read_recipes(path):
    for filename in os.listdir(path):
        file_path = os.path.join(os.path.abspath(path), filename)

        if os.path.isfile(file_path):
            #print("Opening " + file_path)
            f = open(file_path)
            recipe_dict = json.load(f)
            f.close()

            #print("Parsing recipe " + file_path)
            parse_recipe(recipe_dict)

read_recipes(".\\recipes")

print("# Shopping List")
for ingredient, info in shopping_dict.items():
    print(f"- {info['quantity']} {info['unit']} {ingredient}")
