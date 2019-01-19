# write python program to display the power of 2 using anonymous function.

terms = int(input("How many terms? : "))
print("Total number of terms: ")

result = list(map(lambda x : x**2, range(terms)))

for i in range(terms):
    print("2 raised to power of ", i, "is ", result[i])
