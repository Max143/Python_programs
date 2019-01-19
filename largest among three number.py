# program to find the largest among three numbers

x = int(input("Enter the first number : "))


y = int(input("Enter the second number : "))



z = int(input("Enter the  third number : "))

def largest_num():
    if x > y and x > z:
        print("x is largest among three number.")
    elif y > x and y > z: 
        print("y is largest among three number.")
    elif z > y and z > x:
        print("z is largest among three number.")
    else:
        print("All are same number.")

largest_num()

