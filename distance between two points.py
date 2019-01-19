#  compute distance between two points 

x = int(input("Pls input x : "))
y = int(input("Pls input y : "))

x1 = int(input("Pls input x1 : "))
y1 = int(input("Pls input x1 : "))

from math import sqrt

distance = sqrt(((x-y)**2) + ((x1-y1)**2))

print(distance)


import math

p1 = [4, 9]
p2 = [6, 6]

distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

print(distance)
