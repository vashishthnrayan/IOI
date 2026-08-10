number_Largest=int(input("Enter the largest number: "))

number_Smallest=int(input("Enter the smallest number: "))


while(number_Smallest):
   number_Store = number_Smallest
   number_Smallest = number_Largest % number_Smallest
   number_Largest = number_Store

print("HCF is",number_Largest)