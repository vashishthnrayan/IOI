def max_ones(n):
    arr = [1] * n + [0 ] + [1] * n
    streak = best =0
    for x in arr :
        if x : streak += 1
        else : streak = 0
        if streak > best : best = streak
    return best

input ("Max_ones(n) finds the longest run of 1s in [ 1.... 1,0,1..1]")
print("max_one(3)" ,max_ones(3))
print("max_one(4)" ,max_ones(4))
n = int(input("Enter n (try 6 or 6 ):"))
gue = input("waht is max_ones(" + str(n) + ")")
input("streak resets to 0 on each 0 - best keeps the highest streak seen.Press enter")
print(" max_ones ("+str(n) + ") = ",max_ones(n),"your guess" , gue)