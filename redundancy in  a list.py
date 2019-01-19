'''
Python Program to Remove the Duplicate Items from a List
'''

lst = [3,5,2,7,5,4,3,7,8,2,5,4,7,2,1]

print(lst)

def method():
  new_lst = []

  for item in lst:
    if item not in new_lst:
      new_lst.append(item)
    
  print(new_lst)

method()
