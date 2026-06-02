pasta_ingredients = {"Pasta", "Tomato Sauce", "Cheese", "Garlic","Basil","Olive Oil","Garlic","Dough"}

print(pasta_ingredients)
print(len(pasta_ingredients))

pasta_ingredients.add("Parmesan")
pasta_ingredients.discard("Dough")

print(pasta_ingredients)

biryani_ingredients = {"Rice", "Chicken", "Yogurt", "Spices","Onions","Garlic","Ginger","Saffron","Tomato Sauce","Garlic"}
all_ingredients = pasta_ingredients.union(biryani_ingredients)
common_ingredients = pasta_ingredients.intersection(biryani_ingredients)
print("All Ingredients: ", all_ingredients)
print("Common : ", common_ingredients)

only_pasta = pasta_ingredients.difference(biryani_ingredients)  
unique_to_each = biryani_ingredients.symmetric_difference(bryani_ingredients)
print("Only Pasta Ingredients: ", only_pasta)

print("Not Shared Ingredients: ", unique_to_each)
