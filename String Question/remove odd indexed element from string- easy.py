'''
Python Program to Remove the Characters of Odd Index Values in a String
'''

string = input("Enter the string: ")

l


st = list(string)

print(lst)


remove = []
for i in range(len(lst)):
  if i == 0:
    pass
  elif i % 2 == 0:
    pass
  else:
    remove.append(i)

print(remove)   # odd index
print(remove[0])

# removing odd inedexed numeber in the string

count = len(remove)
print(count)

while(count >= 0):
  lst.pop(count)
  count -= 1
print(lst)
print("".join(lst))

print("--------------book method------------------")


def modify(string):  
  final = ""   
  for i in range(len(string)):  
    if i % 2 == 0:  
      final = final + string[i]  
  return final
string=raw_input("Enter string:")
print("Modified string is:")
print(modify(string))



  
