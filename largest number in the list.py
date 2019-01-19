 # write a python program to find the largest number in the list

# using function
a = []
n = int(input("How many time? "))

for x in range(n+1):
    num = int(input("Enter the number to append in the lsit: "))
    a.append(num)
    print(a)
1
# Till here, we have defined the list now find the largest num from the formed list

def largest():
    a.sort()
    print()
print("The largest number from the list: ", largest())


print("-----------------------------------")

print("Another method")

a = []
n = int(input("Enter no. "))

for i in range(int(input("Enter the number of times: "))):
    b = int(input("Enter the element: "))
    a.append(b)
    print(a)


a.sort()
print("Largest number in the list is: ", a[n-1])




print("Use another method to find the largest number in the list")
















