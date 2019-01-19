'''
Python Program to Print Table of a Given Number
'''


def main():
  num = int(input("Enter the number to get the table: "))
  for n in range(1,11):
    print("{0} X {1} = {2}".format(num, n, num*n))


main()

  
