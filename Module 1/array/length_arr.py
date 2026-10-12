def left_rotate(n):
    arr = [1,2,3,4,5]
    n  = n % len(arr)
    return arr[n:] + arr[:n]

input ("Left_rotete(n) shift [1,2,3,4,5] left by n prositions .press enter")
print(" left _rotate(1)",left_rotate(1))
print(" left_rotate(2)",left_rotate(2))
n = int(input("Rotate by how many ? (try 3 or 4)?"))
guess =  input("What is left_rotate (" + str(n)+")")
input("slice from index n to end ,then attach the first n elcemnets .Press enter ")
print("Left _rotate ("+ str(n)+") = ",left_rotate(n),"your guess:",guess)