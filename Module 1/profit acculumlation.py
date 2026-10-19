def total_pro(n):
    prices = [ 1 ,n ,1, n,1]
    profit = 0 
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            profit = prices[i] - prices [ i - 1]
    return profit

input("total profit(n) sums every upswing in prices [ 1 , n ,1 ,n ,1] . press enter")
print ("        total prfit( 4)", total_pro(4))
print ("        total_prfot(5)" , total_pro(5))
n = int(input("Enter n (try  6 or 7)"))
guess = input("what is the total profit("+ str(n)+" ) ? ")
input("add every positive(+) two peaks each contribute n-1.Press enter ")
print(f"max_profit({n}) = {total_pro(n)} | Your guess: {guess}")

