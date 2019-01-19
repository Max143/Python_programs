# Write a python program to search the number of Times a paricular number in a list
'''
a = []
n = int(input("Enter a no. of element: "))

for i in range(n+1):       #(n+1) here I can use input function but this is different method
    b = int(input("Enter element: "))
    a.append(b)
    print(a)

k = 0
num = int(input("Enter the number to be counted: "))
for j in a:
    if(j==num):
        k = k+1

print("No. of times ", num, " appear is ", k)

print("-------------------------------------------")

a = []
for i in range(int(input("How many element in the list? "))):
    b = int(input("enter the element to be appear in the list: "))
    a.append(b)
    print(a)

k = 0
num = int(input("Enter the numbe to be counted: "))
for j in a:
    if(j==num):
        k += 1

print("No. of times ", num, "appear is ",
k)
'''
print("======================================")
print("Write a python program to search the number of times a particular number is presentt in the list. ")




a = []
for i in range(int(input("Enter no. of element to be listed in the list: "))):
    b = int(input("Ënter the elemetn to append in the list: "))
    a.append(b)
    print(a)

num = int(input("Enter the number to be counted: "))

repeated_num = 0

for repeat in a:
    if repeat == num:
        repeated_num += 1

print("No. of times ", num, " appears in the list ", repeated_num)











































