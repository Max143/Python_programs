# Simple Interest
#Formula- s = prt (principal , rate, time)

# Below program has wrong formula but the process is right
# Change the formula to get the correct the value

'''
Write a program to calculate any attribute of simple interest missing.
'''

value  = {
    's' : 'simple interest',
    'p' :  'principal',
    'r' : 'rate',
    't' : 'time',
    'principal' :  'p',
    'rate' : 'r',
    'time' : 't'
    }

print("what you want to calculate?")
def main():
  choice = input("p or r or t or s : ")
  if choice == 's':
    print("To calculate the simple interest: ")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate: "))
    time = int(input("Enter the time(year): "))
    si = (principal*rate*time)/100
    print("Simple Interest is: {}".format(si))
  elif choice == 'p':
    print("To calculate the principal: ")
    simple_interest = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate: "))
    time = int(input("Enter the time(year): "))
    principal = (simple_interest/(1+rate*timt))
    print("Principal: {}".format(principal))
  elif choice == 'r':
    print("To calculate the rate: ")
    simple_interest = float(input("Enter the principal amount: "))
    principal = float(input("Enter the rate: "))
    time = int(input("Enter the time(year): "))
    rate = (1/time)*(simple_interest/principal - 1)
    print("Rate: {}".format(rate))
  elif choice == 't':
    print("To calculate the time: ")
    rate = float(input("Enter the rate: "))
    principal = float(input("Enter the principal amount: "))
    simple_interest = float(input("Enter the simple interest: "))
    while simple_interest < principal:
      print("Simple Interest is greater than principal. Please Enter again!")
      simple_interest = float(input("Enter the simple interest amount greater than principal: "))
    time = (1/rate)*(simple_interest/principal - 1)
    print("Time: {}".format(time))


main()


