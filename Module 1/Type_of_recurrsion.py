# tail Recussion 
def tail(n):


    if (n!=0):
        print(n)
        tail(n-1)

x = int(input("Enter a number: "))

print("Here It is!")
tail(x)

# Head Recursion 

def head(n):
    if (n!=0):
        head(n-1)
        print(n)

x1 = int(input("Enter a number: "))
print("Here It is!")
head(x1)
# Tree Recursion 

def tree(n):

    if (n!= 0 ):
        print(n)
        tree(n-1)
        tree(n-1)

x2 = int(input("Enter a number: "))
print("Here It is!")
tree(x2)

# linear Recursion

def tail_num(n ,acc = 0):
    if n == 0:
        return acc
    else:
        return tail_num(n-1, acc+n)

input("Enter a number: ")
print( " tail_sum(4) = ", tail_num(4), " = 4 + 3 + 2 + 1 + 0 ")
print( " tail_sum(5) = ", tail_num(5), " = 5 + 4 + 3 + 2 + 1 + 0 ")

n = int(input("Enter a number (Try 3 or 6): "))
guess = input ("what is tail_num("+str(n)+")? ")
input("Tial_sum adds n to acc at each step - acc builds as n count down . press Enter ")
print("  tail_sum ("+str(n)+") = ", tail_num(n), " your Guess ",guess )