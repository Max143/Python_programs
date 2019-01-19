# program to find the factorial of a number

num = int(input("Enter a number : "))

def ashi():
    for i in range(1, num+1):
        if num % i == 0:
            print(i)

ashi()

num = int(input("Enter a number : "))

def mansi():
    print("The factor of a %s is : " % (num))
    for i in range(1, num+1):
        if num % i == 0:
            print(i)

mansi()
