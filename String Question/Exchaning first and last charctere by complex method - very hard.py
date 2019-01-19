'''
Python Program to Form a New String where the First Character and the Last Character have been Exchanged
'''

string = input("Enter the string: ")
new = []

for char in string:
  new.append(char)


temp = new[0]
new[0] = new[-1]
new[-1] = temp

print("Entered string by you is: ",string)
print("Updated string: ", "".join(new))

print("-----------------------")

def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_sring('abcd'))
print(change_sring('12345'))






