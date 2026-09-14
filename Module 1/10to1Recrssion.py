def print10to1(n):
    if n < 1:
        return
    print(n)
    print10to1(n - 1)

print10to1(10)