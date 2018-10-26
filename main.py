import geometry


data = input ("Enter the radius of a circle:")
radius = float(data)
print("Area of the circle: {:.2f}".format(geometry.area_circle(radius)))