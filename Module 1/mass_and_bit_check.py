input("Build a bit mask - one 1 at exately that position. Please Enter")
for k in range(4):
    mask = 1 << k
    print("bit ",k," mask = ",mask,"binary:",bin(mask)[2:])

    n =int(input("Enter a number (try 4 or 6)"))
    guess=input("Is it a power of 2? (y/n)")
    input ("check if the nth bit is set - AND with the mask. Press enter")
    result = (n>>2)&1
    if result:
        print(" ",n ,"  Binary :", bin(n)[2:],"  nth bit is set your guess:",guess)

    else:
        print(" ",n ,"  Binary :", bin(n)[2:],"  nth bit is NOT set your guess:",guess)
        