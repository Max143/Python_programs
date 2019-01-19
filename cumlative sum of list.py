'''
Python Program to Find the Cumulative Sum of a List where the ith Element is the 
Sum of the First i+1 Elements From The Original List

cumulative means increasing or increased in quantity

('The original list is: ', [1, 2, 3, 4, 5])
('The new list is: ', [1, 3, 6, 10, 15])

'''
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print("The original list is: ",a)
print("The new list is: ",b)