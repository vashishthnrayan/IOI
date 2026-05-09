it= int(input("Enter the number of rows: "))

for i in range(1,it+1):
    for j in range(i ):
        print("*", end=" ")
    print()  # Move to the next line after each row
