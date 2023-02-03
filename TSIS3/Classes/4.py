'''4. Write the definition of a Point class. Objects from this class should have a

        a method show to display the coordinates of the point
        a method move to change these coordinates
        a method dist that computes the distance between 2 points'''



import math


class Point(object):
    

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def show(self):
        return self.x, self.y


    def move(self, x, y):
        self.x += x
        self.y += y


    def dist(self, pointt):
        dx = pointt.x - self.x
        dy = pointt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)


'''p = Point(12,3)

print(p.show())

p.move(1,1)
print(p.show())
'''

point = Point(1,1)
p = Point(0,0)

print(p.dist(point))

