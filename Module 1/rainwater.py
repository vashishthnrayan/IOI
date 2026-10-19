def rainwater(n):
    bars = [0,n,0,n,0]
    return min(max(bars[:3]),max(bars[2:])) - bars[2]

input("rainwater(n ) traps water between 2 bars of height n .Press Enter " )
print("     rainwater(3)",rainwater(3))
print("     rainwater(4)",rainwater(4))
n= int(input("enter the height (try 5 or 6)"))
guess = input("what is rainwater (" + str(n) + ") ?")

input("water = min(left tallest ,right tallest ) - bars height at the gap .press enter ")
print(f"max_profit({n}) = {rainwater(n)} | Your guess: {guess}")
