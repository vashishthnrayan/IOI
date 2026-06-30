n = 4

total = n * ( n + 1)//2
# 1
print("formula way : total =",total,"| steps = 1")


total= 0 
steps= 0
# 2
for round_num in range (1,n + 1):
    total += round_num
    steps += 1
print("Loops way     : total = ",total, "| steps = ", steps)

 
total = 0
steps = 0
# 3
for round_num in range(1,n+1):
    for point in range(1,round_num +1):
        total += 1 
        steps += 1 
print("Nested loops : total = ",total , "| steps = ",steps)