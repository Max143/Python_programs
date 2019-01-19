# CALCULATE THE AREA OF TRIANGLE


def triangle_area(base, height):
    return base * height / 2

print(triangle_area(10, 5))


b = int(input("Base : "))
h = int(input("Height : ")) 

area_triangle = b * h / 2

print("The area of triangle with Base %d and with Height %d is %d." % (b, h, area_triangle))
