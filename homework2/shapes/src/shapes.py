from math import pi

# TODO: line color
# TODO: fill color
# TODO: shape registration
# TODO: export to file
# TODO: tests


class Shape(object):
    def __init__(self, *args):
        'ok'

    def type_name(self):
        return 'Shape'

    def description(self):
        return 'an abstract shape'

    def full_description(self):
        return self.type_name() + ' - ' + self.description()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


shape = Shape()
print("Shape type: %s" % (shape.type_name()))
print("Shape description: %s" % (shape.description()))
print("Shape full desc: %s" % (shape.full_description()))
shape.name = 'My first abstract shape'
print("Shape name: %s" % (shape.name))


class StraightLine(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def type_name(self):
        return 'Straight line'

    def description(self):
        return 'two dots connected by one straight line'


shape = StraightLine([-1, -1], [1, 1])
print("Shape type: %s" % (shape.type_name()))
print("Shape description: %s" % (shape.description()))
print("Shape full desc: %s" % (shape.full_description()))


class BrokenLine(Shape):
    def __init__(self, dots):
        self.dots = dots

    def type_name(self):
        return 'Broken Line'

    def description(self):
        return 'multiple dots connected by straight lines'


shape = BrokenLine([[1, 1], [3, 3], [3, 2], [2, 3], [3, 3]])
print("Shape type: %s" % (shape.type_name()))
print("Shape description: %s" % (shape.description()))
print("Shape full desc: %s" % (shape.full_description()))


class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return pi*self.radius**2

    def type_name(self):
        return 'Circle'

    def description(self):
        return 'all the dots in a distance of radius from the center'


shape = Circle([0, 0], 1)
print("Shape type: %s" % (shape.type_name()))
print("Shape description: %s" % (shape.description()))
print("Shape full desc: %s" % (shape.full_description()))
print("Shape area: %s" % (shape.area()))


class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def type_name(self):
        return 'Rectangle'

    def description(self):
        return 'defined by two dots on opposite sides of one diagonal'


shape = Circle([-1, -1], [1, 1])
print("Shape type: %s" % (shape.type_name()))
print("Shape description: %s" % (shape.description()))
print("Shape full desc: %s" % (shape.full_description()))
