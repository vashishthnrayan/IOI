def group_reverse(n):
    arr = [1,2,3,4,5,6]
    for i in range ( 0 , 6 ,n):
        arr[i:i+n] = arr [i:i+n][::-1]
    return arr

input("group_reverse(n) reverse[1,2,3,4,5,6] in chunks of n .Press enter   ")
print("     group_reverse(2)",group_reverse(2))
print("     group_reverse(3)",group_reverse(3  ))
n = int(input("Group size (try 1 or 6)?"))
guess =  input("what is the group_revers (" + str(n)+")")
input("each chunk of n element is flipped in place .Press Enter")
print ("    gropu_Reverse("+ str(n) + ") = ", group_reverse(n), "Your guess",guess)