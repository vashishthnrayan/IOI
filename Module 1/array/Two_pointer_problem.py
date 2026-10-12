def reverse (n):
    arr,i,j = list(range(1,n + 1 )),0 ,n-1
    while i < j:
        arr[i], arr[j]  =  arr [j] ,arr[i]
        i += 1;j-=1
    return arr

input  ("Reverse(n) builds [1....n] and flips it end-to-end using two pointers.press enter")
print(" Resvers(4)",reverse(4))
print(" Reverse(5) ",reverse(5))

n= int(input("Enter liost size (try 6 or 7):"))
guess = input("What is resverse("+str(n)+")  ")

input("Left and right swap and move inwards until they meet in the middle . Press Enter ")
print("Reverse"+ str(n) + "/",reverse(n),"Your guess:", guess)