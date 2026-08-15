from math import sqrt



print("\n")


for number in range (2, 100):

        for i in range (2, int(sqrt(number))+1):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break

        else:
            print(number, "is a prime number")
