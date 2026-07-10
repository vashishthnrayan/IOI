names= ['Arav','Priya','Ravi','Ananya','Karan']


target_name = 'Arav'
steps=0
for name in names:
    steps +=1
    if name == target_name:
        break

print('Target       :',target_name)
print('Steps taken  :',steps,'(best case =1)')
print('Big-O        : Omega(1)')