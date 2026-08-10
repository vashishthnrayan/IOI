n = int(input("Enter a number: "))
Original_number  = n
Reversed_number = 0

while n > 0:
    digit = n % 10
    Reversed_number = Reversed_number * 10 + digit
    n //= 10

if Original_number == Reversed_number:
    print(f"{Original_number} is a palindrome number.")
else:
    print(f"{Original_number} is not a palindrome number.")