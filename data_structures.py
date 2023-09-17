spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names_list = []
    for food in spicy_foods:
        names_list.append(food["name"])
    return names_list
get_names(spicy_foods)
    

def get_spiciest_foods(spicy_foods):

    spiciest_foods_list = []

    for food in spicy_foods:
        if food.get("heat_level", 0) > 5:
            spiciest_foods_list.append(food)
    return spiciest_foods_list


def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        name = food.get("name", "Unknown")
        cuisine = food.get("cuisine", "Unknown")
        heat_level = food.get("heat_level", 0)
        chili_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {chili_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine_to_find):
    matching_food = None
    for food in spicy_foods:
        if food.get("cuisine") == cuisine_to_find:
            matching_food = food
            break
    return matching_food

print(get_spicy_food_by_cuisine(spicy_foods, "mboga"))




def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)  # Get the spiciest foods using the existing function

    for food in spiciest_foods:
        name = food.get("name", "Unknown")
        cuisine = food.get("cuisine", "Unknown")
        heat_level = food.get("heat_level", 0)

        chili_emojis = "🌶" * heat_level

        print(f"{name} ({cuisine}) | Heat Level: {chili_emojis}")


def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  

    total_heat = sum(food.get("heat_level", 0) for food in spicy_foods)
    average_heat = total_heat / len(spicy_foods)
    return int(average_heat)  
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


