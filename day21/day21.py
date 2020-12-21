from collections import defaultdict

TEST_INPUT = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()


def parse_food(food):
    food = food.strip()
    if " (contains " in food:
        ingredients, allergens = food.split(" (contains ")
        ingredients = ingredients.split()
        allergens = allergens.rstrip(")").split(", ")
    else:
        ingredients = food
        allergens = []
    return ingredients, allergens


def parse_foods(foods):
    parsed_foods = []
    allergens_to_food = defaultdict(list)
    for food in foods:
        ingredients, allergens = parse_food(food)
        for allergen in allergens:
            allergens_to_food[allergen].append(set(ingredients))
        parsed_foods.append(set(ingredients))
    return allergens_to_food, parsed_foods


def build_allergens_mapping(foods):
    allergens_to_food, _ = parse_foods(foods)

    d = {}
    for allergen, foods_with_that_allergen in allergens_to_food.items():
        d[allergen] = set.intersection(*foods_with_that_allergen)

    def remove_ingredient_from_other_suspects(ingredient):
        removed = False
        for suspect_ingredients in d.values():
            if len(suspect_ingredients) > 1 and ingredient in suspect_ingredients:
                suspect_ingredients.remove(ingredient)
                removed = True
        return removed

    removed = True
    while any(len(ingredients) > 1 for ingredients in d.values()) and removed:
        removed = False
        for allergen, suspect_ingredients in list(d.items()):
            if len(suspect_ingredients) == 1:
                ingredient_with_allergen, = suspect_ingredients
                if remove_ingredient_from_other_suspects(ingredient_with_allergen):
                    removed = True
                    break

    import pdb; pdb.set_trace()
    return d


def part1(foods):
    allergens_to_food, parsed_foods = parse_foods(foods)
    allergens_mapping = build_allergens_mapping(foods)

    ingredients_associated_with_an_allergen = set.union(*allergens_mapping.values())

    count = 0
    for food in parsed_foods:
        for ingredient in food:
            if ingredient not in ingredients_associated_with_an_allergen:
                count += 1
    return count


def test_part1():
    allergens_mapping = build_allergens_mapping(TEST_INPUT)
    assert {'dairy': {'mxmxvkd'}, 'fish': {'sqjhc'}, 'soy': {'fvjkl'}} == allergens_mapping

    assert 5 == part1(TEST_INPUT)


if __name__ == "__main__":
    input_ = open("input21.txt").readlines()
    print("Part 1:", part1(input_))
