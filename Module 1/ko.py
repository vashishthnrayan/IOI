names= ['Arav','Priya','Ravi','Ananya','Karan']
scores= [100, 200, 150, 300, 250]
n = len(scores)

target_name = 150
steps=0
print("paris with total score = ", target_name,":")
for i  in range(n):
    for j in range(i+1,n):
        steps += 1
        if scores[i] + scores[j] == target_name:
            print("(",names[i],",",names[j],"=",scores[i]+scores[j],")")

print("Total comparisons :",steps,"| O(n^2)  -  drop constent , keep n^2  ")
print()