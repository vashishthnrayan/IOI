input(" A set with n elemnets has 2^n subsets.press enter to continue ")
print("  3 elements set has 2^3 = ", 2**3, " subsets")
print("  marks 5 = binary , ",bin (5)[2:],"select positions 0 and 2")

n = int(input("enter a number (try 3 or 5):"))
guess = input( " how many subsets does a set with " + str(n) + " elements have? : ")
input("press enter to see the answer ")
print(" 2^",n," = ",2**n,"your guess was : ",guess)