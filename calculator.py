# Write a prorgam to make simple calculator
# Make an app related to calculator?

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def power(x,y):
    return x**y


print("Select the Operator : ")
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Divison")
print("5) Power")

while True:
    choice = input("Enter the choice (1/2/3/4/5/quit Quit or Q or q or QUIT)")

    if (choice == '1') or (choice == '2') or (choice == '3') or (choice == '4'):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    elif choice == '5':
        number = int(input("Enter the number to find the power of: "))
        pwr = int(input("Enter the power :"))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1,num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1,num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1,num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1,num2))
    elif choice == '5':
        print(number, "to the power of ", pwr, "is", power(number,pwr))
    elif (choice == 'quit') or (choice == 'Q') or  (choice == 'Quit') or  (choice == 'QUIT') or  (choice == 'q'):
        print("Thank your using our calculator.")
        break     
    else:
        print("Invalid Input")






    
