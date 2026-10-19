def max_profit(n):
    prices =list(range(n,0,-1))+ list(range(1,n+1))
    min_prices,profit= prices[0],0
    for p in prices[1:]:    
        min_prices=min(min_prices,p)
        profit=max(profit,p-min_prices)
    return profit

input("max_profit(n) finds the best single buy-sell in prices [n..1,n...2,n...3] .prees enter ")

n = int(input("Enter n (try 6 or 7 )"))

guess =input("What is the max profit (" + str(n) + ") ?")
input("track min price so far - sell when the gap beat the current best  .Press Enter ")
print(f"max_profit({n}) = {max_profit(n)} | Your guess: {guess}")