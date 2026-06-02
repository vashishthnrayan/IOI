pasta = ("Pasta Arrabit", "Italian", 20, "Medium")
chicken_bryani = ("Chicken Biryani", "Indian", 15, "Spicy")
print("Recipe 1  ", pasta)
print("Name: ", pasta[0])
print("Cuisine: ", pasta[1])
print("Difficulty: ", pasta[3])


print("Recipe 2  ", chicken_bryani)
print("Name: ", chicken_bryani[0])
print("Cuisine: ", chicken_bryani[1])
print("Difficulty: ", chicken_bryani[3])


print("\n pasta recipes :")

for details in  pasta:
    print(" - ",details)

pasta_ingredients = {"Pasta", "Tomato Sauce", "Garlic", "Olive Oil", "Basil"}
biryani_ingredients = {"Rice", "Chicken", "Yogurt", "Spices", "Onions", "Garlic", "Ginger", "Saffron", "Tomato Sauce"}

print("\n Pasta Ingredients: ", pasta_ingredients)
print("\n Biryani Ingredients: ", biryani_ingredients)
print("Total pasta Ingredients: ", len(pasta_ingredients))



pasta_ingredients.add("Parmesan")
pasta_ingredients.discard("Dough")
print("\n Updated Pasta Ingredients: ", pasta_ingredients)


all_ingredients = pasta_ingredients.union(biryani_ingredients)
common_ingredients = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = biryani_ingredients.symmetric_difference(biryani_ingredients)

print("\n All Ingredients: ", all_ingredients)
print("\n Common Ingredients: ", common_ingredients)
print("\n Only Pasta Ingredients: ", only_pasta)