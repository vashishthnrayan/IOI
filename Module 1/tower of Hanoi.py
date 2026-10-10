def hanoi(n):
    if n == 0 :
         
         return 0
    return 2 * hanoi(n - 1) + 1

input("Hanoi(n) count the mi disk form on page to another . pree enter ")

print("Hanoi(1)  =  " , hanoi(1) )
print(" Hanoi(2) = ", hanoi(2))

n = int(input("Enter the number of disk (tey 3 or 4)"))
g = input (f"What is Hanoi According to u {str(n)}?\n ")
input("hanot(n) = 2  * hanoi(n-1 ) + 1  move the stacks twice plus big  disk once")
print(f"hanoi{str(n)} =  { hanoi(n)} ,      your guess {g}")