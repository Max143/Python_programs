'''
Python Program to Put Even and Odd elements in a List into Two Different Lists
'''

even = []
odd = []

n = int(input("Enter the number you want in list: "))

for n in range(n):
  num = int(input("Enter the number: "))
  if num % 2 == 0:
    even.append(num)
  elif num % 3 == 0:
    odd.append(num)
  
print(even)
print(odd)

print(Another method)

lst = []
for i in range(n):
  num = int(input("Enter the number: "))
  lst.append(num)

for number in lst:
  if number % 2 == 0:
    even.append(number)
  else:
    odd.append(number)  
print(lst)
print(even)
print(odd)
  
