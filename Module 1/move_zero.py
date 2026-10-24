def move_zero(n):
    arr = [ 0 ,1 ] * n
    write = 0 
    for x in arr :
        if x : arr[write] = x ; write += 1


    arr [ write : ] = [0] *  ( len (arr) -write)
    return arr

input ( "Move_zeros (n) move all zero to end of [0,1,0,1...] . press enter")
print ("move_zero(3)", move_zero(3))

print ("move_zero(4)", move_zero(4))

n =int(input("Enter n (try 5 or 6):"))
gu = input("what is movce_zeros(" + str(n) + ") ?")

input("write pointer collects non-zeros - fill the rest with zeros .Press enter")
print(" move_zeros(" + str(n) + " ) = ",move_zero(n) , "your guess" ,gu)
