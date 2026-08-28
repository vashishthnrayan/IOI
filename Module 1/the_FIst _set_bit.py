input("first set bit - the rihtmost 1 in the binary number. Please Enter")
print("    5 = ",bin(5)[2:],"first 1 at position 0")
print("    8 = ",bin(8)[2:],"first 1 at position 3")


n=int(input("Enter a number (try 8 or 14):"))

input("Watch bits drop until the first 1 is found. Press enter")

temp = n
pos=0

while temp>0:
    print("  binary:",bin(temp)[2:],"  last bit:",temp & 1)
    if temp & 1:
        break
    pos+=1
    temp >>= 1
print("first set bit in ", n , " is at position", pos)