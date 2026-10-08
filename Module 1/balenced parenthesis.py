def count_parn(n , l = 0 , r = 0 ):
    if l == n and r == n:
        return 1
    total = 0
    if l < n:
        total += count_parn(n , l + 1 , r)
    if r < l:
        total += count_parn(n , l , r + 1)

    return total

input("count_parn counts the number of balanced parenthesis for n pairs of parenthesis. Press enter")
print("count_parn(3)=",count_parn(3))
print("count_parn(4)=",count_parn(4))

n= int(input("Enter the number of pairs (3 or 4): "))
gueess = input("what is count_parn(" + str(n) + ")?")
input("count_parn counts the number of balanced parenthesis for n pairs of parenthesis. Press enter")
print("count_parn(",str(n),")=",count_parn(n),"your guess ",gueess)