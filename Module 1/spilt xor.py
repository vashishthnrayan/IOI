input("XOR all -pairs cancel, the odd one stays. Press enter to continued")
print("[1,4,3,3] XOR of all:",1^4^3^3,"binary:",bin(1^4^3^3)[2:])

print( " split bit 1   ->groups A (bit 0 ON): 1  groups 8(bits 0 OFF): 4")


n = int(input("enter a number (try 6 or 9)"))
guess = input("it is 0 of "+ str(n) + " ON? ?(y/n)")
input("check the split bit . press enter ")
if n & 1:
    print(" ", n, "binary : ", bin (n)[2:],"bit 0 On - group a your guess",guess)
else:
    print("  ", n ," binary : ",bin(n)[2:],"bit - off - groups b your guess:",guess)