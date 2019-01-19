'''
Python Program to Find the
sort element in the list (smaller to largest)
sort element in the list (largest to smalles)
Largest Number in a List
smallest number in a list
2nd largest number in a list


'''

#n = int(input("Enter the number of element you want in the list: "))
'''
uncomment for user given input
n = 7
lst = []

for number in range(n):
  num = int(input("Enter the number now: "))
  lst.append(num)
'''


# sort(argument)  smallest to largest
# sorted(argument, reverse = True)



lst = [34,27,54,656,244,344,45,23]
print("Here is the list: {}".format(lst))


lst.sort()  # sorting in the form list


print("Sorting (smallest to largest): {}".format(lst))


largest_to_smallest = sorted(lst, reverse = True)
print("Sorting (largest to smallest): {}".format(largest_to_smallest))


print("Largest number in a list: {}".format(lst[-1]))


print("2nd Largest number in a list: {}".format(lst[-2]))


print("smailles number in a list: {}".format(lst[0]))
