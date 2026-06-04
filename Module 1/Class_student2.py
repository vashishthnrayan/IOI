class Students :

    

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def intro(self):
        print("Hello, I am ", self.name, "and I am ", self.age, "years old and my grade is ", self.grade)

student1 = Students("Vas", 20, 85)
student2 = Students("Aviral", 22, 90)
student1.intro()
student2.intro()

