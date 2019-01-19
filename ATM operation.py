#write a python program for ATM trsansfer mode

print("This how ATM works.\n")

print("welcome to atm \n")

print("Swipe your card\n")

print("Availabe operation")
Transaction = ['balance enquiry', 'withdraw mooney', 'deposit', 'chnange your pin', 'quit']
# converting in to stack form by using loop

for operation in Transaction:
    print(operation)
atm_pin = 9999
'''
def new_input():
    atm_pin.append(new_input)
    print("This is your new pin. Remember this.", + atm_pin)
    print("pin successfuly chnaged. Try again")

'''
print("\n")
pin = int(input("Enter you 4 digit pin: "))
if pin == 9999:
    print("Please select your transaction: ")
    print("1. Balance Enquiry")
    print("2. Withdraw Money")
    print("3. Deposit")
    print("4. Change your pin")
    print("4. Quit")

   
    trans = input("Select the operation: ")
    if trans == "balance enquiry":
        answer = print("Do you want recipt.(yes or no)")
        if answer == yes:
            print("Printing")
        else:
            print("Thanks for using ATM")
            
    elif trans == "withdraw money":
        amount = int(input("Enter the amount: "))
        if amount > 0:
            print("Collect your amount. Thank you for using ATM")
        else:
            print("Invalid Input")
            
    elif trans == "deposit":
        amount = int(input("Enter the amount: "))
        if amount > 0:
            print("You amount deposite. Thank you usingn atm.")
        else:
            print("Invalid Input")

    elif trans == "change your pin":
        old_pin = int(input("Enter you old pin: "))
        if old_pin == 9999:
            new_input = int(input("Enter your new pin to setup. And please remember pin."))
            if new_input == 9999:
                print("used pin")
            elif (new_input > 999):
                new_pin = print("your new pin is ", new_input)
        else:
            print("wrong input")


    elif trans == "quit":
        print("Thank you for using our ATM.")

    else:
        print("Invalid inout! No such operation! Please select the list of given operation")


              
else:
    print("Wrong Input, Try again")



