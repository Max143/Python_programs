'''
Python program to print identity matrix
'''

# Driver Code         

def identity(size):
    for row in range(0,size):
        for col in range(0, size):

            # Here end is used to stay in same line
            if (row==col):
                print("1", end=" ") 
            else:
                print("0", end=" ")
        print()



# Driver Code
size = 5
identity(size)

print("--------------------")

print("Program to check whether the matrix is identity or not.")



def isidentity(mat, N):
    for row in range(N):
        for col in range(N):
            if row == col and mat[row][col] != 1:
                return False
            elif row != col and mat[row][col] != 0:
                return False
    return True

N = 4
mat = [[1, 0, 0, 0], 
       [0, 1, 0, 0], 
       [0, 0, 1, 0], 
       [0, 0, 0, 1]]


if(isidentity(mat, N)):
    print("Yes")
else:
    print("No")


print("-----------------------")











print("-----------------------")
print("Matrix Operation")



import numpy # initializing numpy for matrix operations


# Now, Initializing matrices
x = numpy.array([[1,3],[2,5]])
y = numpy.array([[4,5],[4,6]])

# Using add() to add matrices
print("Addition: ", add(x,y))

# Using Subtract() to matrices
print("Subtraction: ", subtract(x,y))

# using divide() to divide matrices
print("Divide: ", divide(x,y))

# The element widse multiplication of matirx is:
print(numpy.dot(x,y))

# The Product of matrice is:
print(numpy.dot(x,y))

# The element wise square root is:
print(numpy.sqrt(x))





















































