pasta = ("Pasta Arrabit", "Italian", 20, "Medium")
print(pasta)
print(pasta[0])
print(pasta[-1])

biryani = ("Biryani", "Indian", 15, "Spicy")

all_dishes = pasta + biryani

print(all_dishes[0][0])
print(all_dishes[1][2])
print(pasta[1:3])

for details in all_dishes:
    print(" - ",details)


