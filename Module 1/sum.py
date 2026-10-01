def sum1to10(n):
    if n > 10:
        return 0
    return n + sum1to10(n + 1)

print(sum1to10(1))
