'''
Python Program to Remove the nth Index Character from a Non-Empty String
'''

def main(string, remove):
  # breaking string into first and last
  first = string[ : remove]
  last = string[remove+1 : ]
  print(first+last)


string = input("Enter the string: ")
remove = int(input("Enter the index to remove from the string: "))

main(string, remove)
