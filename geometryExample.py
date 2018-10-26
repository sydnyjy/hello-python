import math

def area_circle (radius):
        return math.pi * radius **2
if ___name___== "__main___":
    print ("This is from geometry.py")

data = input ("Enter the radius of a circle:")
radius = float(data)
print("Area of the circle: {:.4f}".format(area_circle(radius)))