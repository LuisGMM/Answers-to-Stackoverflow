

fridge = {
    "orange" : 5,
    "citron" : 3,
    "sel" : 100,
    "sucre" : 50,
    "farine" : 250,
    "lait" : 200,
    "oeufs" : 1,
    "tomates" : 6,
    "huile" : 100,
}
    
recipes = {
    "jus_de_fruit" : {
        "orange" : 3,
        "citron" : 1,
        "pomme" : 1
    },
    "salade" : {
        "tomates" : 4,
        "huile" : 10,
        "sel" : 3
    },
    "crepes" : {
        "lait" : 400,
        "farine" : 250,
        "oeufs" : 2
    }
}

def in_fridge(ingredients: dict, fridge_food: dict) -> bool:
    for ingredient in ingredients:

        if ingredient not in fridge_food:
            return False

        if ingredients[ingredient] > fridge_food[ingredient]:
            return False

    return True

def check_recipes(recipes: dict, fridge_food: dict) -> list:

    ans = []
    for recipe in recipes:

        if in_fridge(recipes[recipe], fridge_food):

            ans.append({recipe: recipes[recipe]})

    return ans


if __name__ == '__main__':

    print(check_recipes(recipes, fridge))
