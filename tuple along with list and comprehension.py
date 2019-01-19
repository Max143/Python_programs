'''
Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number

output: 
[(1, 1), (2, 4), (3, 9), (4, 16)]
'''

lower = int(input("Enter the lower number: "))
upper = int(input("Enter the upper number: "))

final = []

for element in range(lower, upper+1):
  tuplex = element, element**2
  final.append(tuplex)


print(final)


print("List Comprehension Method")

l_range=int(input("Enter the lower range:"))
u_range=int(input("Enter the upper range:"))

a=[(x,x**2) for x in range(l_range,u_range+1)]

print(a)


print("List comprehension simplified version")
l = 1
u = 5

a = []

for x in range(l,u+1):
  tup = x, x**2
  a.append(tup)
  ,,k
print(a)
