'''
Working With List
'''

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(list)

list.insert(list.index(input("Enter the element you want to replace: ")), input("Enter the element you want to place: "))

print(list)


print(list)

# appending which means adding at the last automatically
print(list.append('h'))

# placing in stack 
for letters in list:
    print(list)
    print(len(list))

print("======================================")

print(list)

# removing and inserting at certain position
list[0] = 1

print("----------------------------------")

print(list)

# appending again 

print(list.append('fuck'))
print(list)

print("tttttttttttttttttttttttttttttttttttttttttttttttt")

# adding at certain position


print("Don't Know !")

# empty the list

list = []
print("empty list " + str(list))

list.append('a')
list.append('b')
list.append('c')
list.append('d')
list.append('e')
list.append('f')
list.append('g')

print(list)

'''
while True:
   list.append(input('Enter the input: '))
   print(list)
'''


print("======================================")

#print in the stack form also count the number of the items in the list 


print(list)

for letter in list:
    print(letter)

print(list)

print("++++++++++++++++++++++++++++++++++++")


# we find the index if the list is short but
# if the list is long then we use index function or method

print(list)

#suppose you have to put the word Fuck before g then
#we do not count index we use index function

# follow the step
# 1. find the index position of letter or item
# 2. use that index position


print("index position of g is " + str(list.index('g')))

# Now, insert fuck before g
# here , use insert function.

list.insert(list.index('g'), 'fuck')

print(list)

print('44444444444444444444444444444444444444444444')


# Repeat the above for practice :

# Put h letter in the last
# Put 1 number in the first
# Put Ashi between d and e is same as adding item at certain position(long list so use index function)
# remove b and insert 2
# empty the list in the last

# (Advanced practice with the list)
# Ask user to input something between g and h.
# Ask user to input something between between random items




list.append('h')
print(list)

list.insert(0, '1')
print(list)


list.insert(list.index('e'), 'Ashi')
print(list)


list[list.index('b')] = 2
print(list)

'''
list = []
print(list)
'''

print('Avanced practice with the list')

#list.insert(list.index('h'), (input('Input here: ')))
print(list)
# in stack
for items in list:
    print(items)
print("No. of items in the list: " + str(len(list)))

#Here we use random function that automatically push the input in the list
#list.insert(list.index(input('Input here:')), (input('Input here: ')))
#print(list)

print("********************************************************************8")

print("Lets do some arithmetic with list")


num_list = [1,2,3,4,5,6,7]
print(num_list)
lst = []
for numbers in num_list:
    product =numbers ** 2  
    lst.append(product)
print(lst)

family = ['mansi', 'Manish', 'Ashi', 'Jessica']

print(family)

# Insert will not remove the element which at index, it will place the element before the index element
family.insert(family.index(input("Enter the element you want to replace: ")), input("Enter the element you want to place: "))

print(family)



























