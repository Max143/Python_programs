# calculating the hypotenus of a right angled-triangle

from math import sqrt
perp = float(input("perpendicual : "))
base = float(input("base : "))

hypo = sqrt(perp ** 2 + base ** 2)

print("The hypotenuse of a right angled-triangle with perpendicular %d and with base %d is %d ." % (perp, base, hypo))


