import math
a = float(input("Enter the area:"))
radius = math.sqrt(a/math.pi)
perimeter = 2* math.pi * radius
print("The perimeter of the given circle with area",a,"is", perimeter)