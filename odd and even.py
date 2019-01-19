# Excercise - 2

print("Odd and Even")


while True:
    user_input = int(input("Enter the number: "))
    if user_input % 2 == 0 :
        print("Entered number is even")
    else:
        print("Entered number is odd")
    if user_input == "quit":
        break
