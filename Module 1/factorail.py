def reccur_Factorial(n):
    if n == 0:
        return 1
    else:
        return n * reccur_Factorial(n - 1)
    
number = int(input("Enter a number: "))

if number < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", number, "is", reccur_Factorial(number))