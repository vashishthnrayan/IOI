input("XOR all numbers - pairs cancel,the  odd one stays . Press enter to continue")
print("   list : [2,3,4,3,2]")
print("   odd-occuring : ", 2^3^4^3^2)

n =int(input("Enter a number (try 7 or 11)"))

nums = [3,n,5,3,5]
guess= input("What is the odd-occuring number in the list : " + str(nums) + "?")
result = 0

for x in nums:
    result ^= x

input("XOR cancels pairs - the odd one survies .Press enter to see the answer")
print("   odd-occuring : ",result,"your guess:",guess,"list",nums)