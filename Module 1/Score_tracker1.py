names= ['Arav','Priya','Ravi','Ananya','Karan']
n = len(names)

target_name = 'Ravi'
steps=0
for name in names:
    steps +=1
    if name == target_name:
        break

print('Target       :',target_name)
print('Steps taken  :',steps,'worst case =',n,')')
print('Big-O        : O(n)')