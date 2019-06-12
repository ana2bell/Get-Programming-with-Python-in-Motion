class Circle(object):
    #how to initalize an object
    def __init__(self):
        # a new circle has an initial radius of 0
        self.radius = 0
    # other methods
    def change_radius(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    
one_circle = Circle()
another_circle = Circle()

one_circle.change_radius(4)
print(one_circle.get_radius())
print(another_circle.get_radius())

c = Circle()
c.change_radius(2)
r = c.get_radius()
print(r)
# following code is the same as above 4 lines
c = Circle()
Circle.change_radius(c, 2)
r = Circle.get_radius(c)
print(r)


class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def set_length(self, length):
        self.length = length
    def set_width(self, width):
        self.width = width
        
a_rectangle = Rectangle(2,4)
#bad_rectangle = Rectangle(2)
