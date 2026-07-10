# Asymptotic simplification  - keep the dominant term:

# 3n^2 + 5n + 9    ->  O(n^2)       (n^2 dominates  for large n)
# 7n   +   100     ->  O(n)         (n dominates for large n)
# n*(n-1)/2        ->  O(n^2)       (expand : n^2 - n / 2 ,dominant term is n^2)
# 500              =>  O(1)         (constant time)


# proof  n=1000

n=1000
total = 3*n**2 + 5*n + 9

dominant  = n**2

print('full expression = ',total)
print('dominant term = ',dominant)
print('ratio = ',round(total/dominant,2))  # ratio = 3.01  (3n^2 dominates for large n)