input ("Head-Tail - head is list [0] tail is list [1] - press Enter ")
print(" [ 10 ,20 ,30  ] head: ", [10,20,30][0]," tail: ",[10,20,30][1:])
print(" [ 5 , 15 ,25] head:", [5,15,25][0]," tail: ",[5,15,25][1:])

list  = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
guess = input("What is the head of  "+ str(list)+" ? ")
input ("Head is the first element of the list - press Enter ")
print("Head of ",list," is ",list[0]," your guess was ",guess)