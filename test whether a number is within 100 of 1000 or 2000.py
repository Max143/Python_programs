# TEST WHETHER A NUMBER IS WITHIN 100 OF 1000 OR 2000

n = int(input("Input integer : "))

def ashi():
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

print(ashi())
