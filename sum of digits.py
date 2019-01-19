# calculate the sum of digit in an integer

x = int(input("x : "))
y = int(input("y : "))
z = int(input("z : "))
m = int(input("m : "))

sum_of_all_digits = x + y +z + m

print("The sum of all four digits is %d " % (sum_of_all_digits))

 

num = int(input("Input a four digit numbers : "))

X  = num // 1000
X1 = (num - X*1000)//100
X2 = (num - X*1000 - X1*100)//10
X3 =  num - X*1000 - X1*100 -X2*1

print("The sum of digits in the number is ", X+X1+X2+X3)




