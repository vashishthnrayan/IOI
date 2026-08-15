a = 10
b= 6

def bits(n):
    binary = ""
    while n > 0 :
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return binary


#  printing output  
print("a = ", a ,"->", bits(a))
print("b = ", b ," ->", bits(b))

# 'And' and 'Or' operation

print(f"And a & b = {a & b} -> {bits(a & b)}")
print(f"Or a | b = {a | b} -> {bits(a | b)}")

# 'not' and 'Xor' operation


print(f"Not a = {~a} -> {bits(~a)}")
print(f"Xor a ^ b = {a ^ b} -> {bits(a ^ b)}")

# 'Left Shift' and 'Right Shift' operation

print("Left Shift a << 1 = ", a<<1,' (a x 2)')
print("Right Shift a >> 1 = ", a>>1,' (a / 2)')

# print even and odd using xor
for  n in (7,10,15,4):
    result = 'even' if n^1 == n +1 else 'odd'
    print(f"{n} -> {result}")


# count bits


def count_bits(n):
    count = 0
    while n> 0 :
        count += 1
        n>>=1
    return count

for n in (a ,b ,35):
    print(n,"->", count_bits(n), "bits |",bits(n ))