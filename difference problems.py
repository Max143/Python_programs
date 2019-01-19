"""
Get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference

"""
number = int(input("please input the number : "))

new_number = 17 - number
print(new_number)

def ashi():
    if number > 17:
        return (17 - number)*2

print(ashi())


def difference(n):
    if n <= 17:
        return 17-n
    else:
        return (n-17)*2

print(difference(22))
print(difference(14))
