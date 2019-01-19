# python program of password generator


import random
s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-'
while True:
    pass_length = int(input("How many character you want in your password?: "))
    if pass_length > len(s):
        print("Password is to long. Try again up to minimum charcter of 73")
    else:
        your_password = ' '.join(random.sample(s, pass_length))
        print(your_password)

print("Another Method")

import random
import string

def pw_gen(chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(int(input("Enter the number of elements: "))))

    print(pw_gen())
"{
print(pw_gen())


