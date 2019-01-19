# adding two matrices using nested loop
"""
x =  ['12', '72', '43']['34', '54', '34']['32', '23', '24']

y =  ['5', '3', '5']['3', '2', '1']['5', '5', '2']

result = x + y
print(result)
"""

x = [['1', '2', '3'],
     ['4', '5', '6'],
     ['7', '8', '9']]

y = [['1', '2', '3'],
     ['4', '5', '6'],
     ['7', '8', '9']]

result = [['0', '0', '0'],
          ['0', '0', '0'],
          ['0', '0', '0']]

#Iterate through rows

for i in range(len(x)):
    # iterate through columns
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

for r in result:
    print(r)
