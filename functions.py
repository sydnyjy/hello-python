def square(x):
    return x * x
    
x = 10
print("{}**2 == {}".format(x, square(x)))

for y in range(10):
    print("{}**2 == {}".format(y, square(y)))