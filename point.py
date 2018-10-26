class Point():
    def __init____(self, x= 0.0, y = 0.0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

p = Point()
print(p)
print(p.x, p.y)
q = Point(3.5, 4.6)
print(q)