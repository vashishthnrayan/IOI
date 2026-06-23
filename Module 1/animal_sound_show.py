from abc import ABC, abstractmethod
from turtle import color

class Animal(ABC):
    def __init__ ( self,name,habitat):
        self.name = name
        self.habitat = habitat
    
    @abstractmethod
    def sound(self):
       pass
    dis
 
class Dog(Animal):
    def __init__ (self,name,habitat,breed):
        super().__init__(name,habitat)
        self.breed = breed

    def sound(self):
        return "Woof!"
    
# parrot

class Parrot(Animal):
    def __init__ (self,name,habitat,phase):
        super().__init__(name,habitat)
        self.phase = phase

    def sound(self):
        return "Squawk!"
    
# LION

class Lion(Animal):
    def __init__ (self,name,habitat ,pride_size,mane_color):
        super().__init__(name,habitat)
        self.pride_size = pride_size
        self.mane_color = mane_color

    def sound(self):
        return "Roar!"

l=Lion("Simba","Savannah",10,"Golden")
p=Parrot("Polly","Tropical Rainforest","Green")
d=Dog("Buddy","Domestic","Golden Retriever")

print("Animal Sound Show:")

print(f"{l.name} the Lion says: {l.sound()}")
print(f"{p.name} the Parrot says: {p.sound()}")
print(f"{d.name} the Dog says: {d.sound()}")

for animal in [l, p, d]:
    animal.sound()
