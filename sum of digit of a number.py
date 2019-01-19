num = int(input("Enter the digits: "))

lst_str = []  # Declaring empty list for string

# Int cannot be scripptible so 
# converting into str and storing each into the list lst_str[]
for digit in str(num):
    lst_str.append(digit)
#print(lst_str)



lst_int = []  # Declaring empty list for integer

# string list cannot be added so 
# Converting into integer list called lst_int[]
for i in lst_str:
    lst_int.append(int(i))
#print(lst_int)



sum = 0  
# Now, adding each item in lst_int[] 
for i in lst_int:
  result = i
  sum = sum + result
print(sum)


print('--------------------Another Method-----------------------------')

# // <- Operator to get whole number on divison
n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)





















