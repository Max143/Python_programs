'''
Python Program to Find the Union of two Lists
'''

a = [2, 4, 6, 3, 6, 7, 9, 10, 5, 8]

b = [2, 12, 17, 5, 19, 20, 9, 6, 11, 18]


# Union of list mean every element occur only once 

lst = a + b

final = []

for element in range(len(lst)):
  if element not in final:
    final.append(element)
  

print(final)



'''
Python Program to Find the Intersection of Two Lists
'''

lst_1 = [2,3,4,5,3,7,8,9]

lst_2 = [4,5,11,15,7,2,8,1]


new = []

for element in lst_1:
  if element in lst_2:
    new.append(element)
  
print("Element that present in both list: ", new)
