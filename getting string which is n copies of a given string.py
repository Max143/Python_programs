#Get a string which is n(non-negative number) copies of a given string

def larger_string(str, n):
    result = " "
    for i in range(n):
        result = result + str
    return result

print(larger_string("abc", 45))


print("--------------")


print(larger_string('mansi', 45))



