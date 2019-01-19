'''
Total divisor of an Integer
Find the largest divisor of an integer
Find the smallest divisor of an integer

'''


num = int(input("Enter the integer: " ))
lst = []

# total divisor of an integer

for i in range(2,num+1):
    if (num%i == 0):
        result = i
        lst.append(result)
print(lst)

# Find the Largest divisor of an integer
# After finding the total divisor sort the list and get the smallest and largest

largest_divisor = lst.sort()
print("Largest Divisor: ",lst[-1])

smallest_divisor = lst.sort()
print("Smallest Divisor: ",lst[0])


        



        
