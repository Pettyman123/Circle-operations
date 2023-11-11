import math
r = float(input("Enter the radius:"))

h= float(input("Enter the height of chord:"))
base = h*h - r*r
ch = 2*(math.sqrt(base))

print("THe lenght of chord is", ch)