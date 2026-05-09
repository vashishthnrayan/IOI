num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

for i in range(1,limit + 1):
    result = num * i
    print(f"{num} x {i} = {result}")