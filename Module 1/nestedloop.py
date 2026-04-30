num=float(input("Enter your age or a even number:"))

# if num>=0:
#     if num>=18:
#         print("Adult")
#     else:
#         print("Minor")
# else:
#     print("Invalid input")

print("Number to be checked:", num)

if num%2==0:
    print("Even number")
else:
    print("Odd number")


num1=float(input("Enter number to check:"))

if num1>=50:
    print("Greater than or equal to 50")
    if num1%2==0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Less than 50")