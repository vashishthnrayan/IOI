a = int(input("Enter the first number(1) for lcm: "))
b = int(input("Enter the second(2) number for lcm: "))

maxNum = max(a, b)

while True: 
    if (a,b) == (0,0):
        print("LCM is not defined for both numbers being zero.")
        break
    if maxNum % a == 0 and maxNum%b == 0:
        break
    maxNum += 1


print("The LCM of", a, "and", b, "is", maxNum)