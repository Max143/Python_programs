'''
Python Program to Print an Inverted Star Pattern

solution example:
Enter number of rows = 5
*****
****
***
**
*

'''


n = int(input("Enter the number of row: "))

for i in range(n,0,-1):
   print((n-i) * ' ', i * '*')
 
'''
Explain:

i will be range from n-1 to o (with decrement by one)
i.e

5
4
3
2
1

in next line, (n-i) will mulitiply with space to provide thoes spaces to be
filled by *.
i.e

(n-1) * ' '   will give:
5 spaces
4 spaces
3 spaces
2 spaces
1 spaces

These spaces will filled by stars *

i * '*'

i.e

5 * '*'  =  *****
4 * '*'  =   ****
3 * '*'  =    ***
2 * '*'  =     **
1 * '*'  =      *

'''

print('--------------------------------------')













































