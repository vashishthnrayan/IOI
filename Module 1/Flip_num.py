def flip_num(n):
    if n // 10 == 0:
        return n
    last = n % 10
    rest = flip_num(n// 10)
    return last * pow(10, len(str(rest))) + rest

input("flipNUmber peel last digit with  % 10 then recurses on // 10.Press Enter")
print("filp Num=(1234)",flip_num(1234))
print("filp Num=(123456789)",flip_num(123456789))

nu=int(input("Enter a number to flip try(123456789 or 1234):  "))
guess = input("Enter the flipped number(" + str((nu)) + "): ")
input ("flip_number peels last digit and places is at the front of each step,press enter")
print("flip_num(",str(nu),")=",flip_num(nu))
