'''
Python Program to Calculate the Length of a String Without Using a Library Function
'''

string = input("Enter the string: ")
print(len(string))   # using built-in function


# without using built-in function 
count = 0
for char in string:
  count += 1

print(count)
