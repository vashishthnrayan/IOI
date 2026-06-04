# class fruit:
#     print("This is a class for fruits")




class fruits:

    taste = "Sweet"

    def __init__(self,name,color):
        self.name = name
        self.color = color

    
    def intro(self):
        print("Hello,I  am ",self.name, "and ,i am ",self.color," in color")

    
apple = fruits("Apple","Red")


banana = fruits("Banana","Yellow") 
apple.intro()
banana.intro()

print(apple.name,"tastes",apple.taste)
print(banana.name,"tastes",banana.taste)