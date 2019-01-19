'''
Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List
'''

import random 

lst = []

n = int(input("Ener the number of elemen you want in the list: "))

for i in range(n):
  lst.append(random.randint(1,20))

print(lst)
