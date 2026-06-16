class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
        

class dog(Animal):
    def __init__(self, name, habitat, breed):
        Animal.__init__(self, name, habitat)
        self.breed = breed
        
class cat(Animal):
    def __init__(self, name, habitat, color):
        super().__init__(self, name, habitat)
        self.color = color

# instance of dog and cat
d= dog("Buddy", "Domestic", "Golden Retriever")
c = cat("Whiskers", "Domestic", "Tabby")


# dog
print(d.name)
print(d.breed)
print(d.habitat)

# cat
print(c.name)
print(c.color)
print(c.habitat)