import geometry


data = input ("Enter the side lenghts of a triangle:")

(a, b, c) = (float(number) for number in (data.split)(","))

P=geometry.triangle_perimeter(a, b, c)
A=geometry.triangle_heronsarea(a,b,c)
print("Perimeter {:.2f}".format(P))
print("Area {:.2f}".format(A)) 