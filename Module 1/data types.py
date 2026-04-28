name= "Penguin"
age = 15
IS_STUDENT = True
weight =  60.5

print("Name : ", name)
print("Data Type of Name is ", type(name))
print("Age : ", age)
print("Data Type of Age is ", type(age))
print("Is Student : ", IS_STUDENT)
print("Data Type of Is Student is ", type(IS_STUDENT))
print("weight : ", weight)
print("Data Type of weight is ", type(weight))

print("\n after Type casting...")
age=    str(age)
print( age)
print("Data Type of Age is ", type(age))
weight = int(weight)
print(weight)
print("Data Type of weight is ", type(weight))