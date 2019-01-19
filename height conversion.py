#convert height into seconds

print("Input your height ")

h_ft = int(input("Feet : "))

h_inch = int(input("Inches : "))

h_inch = h_inch + h_ft * 12

h_cm = round(h_inch * 2.54, 1)
"""
here, instead of using float, we use round.
This is bcuz float tkes at most 1 argument
"""

print("your hieght is : %d cm." % h_cm)




 

