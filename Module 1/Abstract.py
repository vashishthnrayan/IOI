from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed

    def speak(self):
        return "Woof!"


d = Dog("Buddy", "Wild", "Golden Retriever")
print(d.name)
print(d.habitat)
print(d.breed)
print(d.speak())