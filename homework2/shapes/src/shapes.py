from math import pi

# TODO: shape registration
# TODO: export to file
# TODO: tests


class Shape(object):
    def __init__(self, *args):
        self.__name = None
        self.__line_color = 'black'

    def type_name(self):
        return 'Shape'

    def description(self):
        return 'an abstract shape'

    def full_description(self):
        return f"{self.type_name()} - {self.description()}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def line_color(self):
        return self.__line_color

    @line_color.setter
    def line_color(self, new_line_color):
        self.__line_color = new_line_color


class StraightLine(Shape):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def type_name(self):
        return 'Straight line'

    def description(self):
        return 'two dots connected by one straight line'


class BrokenLine(Shape):
    def __init__(self, dots):
        super().__init__()
        self.dots = dots

    def type_name(self):
        return 'Broken Line'

    def description(self):
        return 'multiple dots connected by straight lines'


class FillableShape(Shape):
    def __init__(self, *args):
        super().__init__()
        self.__fill_color = 'white'

    def type_name(self):
        return 'Abastract fillable shape'

    def description(self):
        return 'closed figure which can be filled with a color'

    @property
    def fill_color(self):
        return self.__fill_color

    @fill_color.setter
    def fill_color(self, new_fill_color):
        self.__fill_color = new_fill_color


class Circle(FillableShape):
    def __init__(self, center, radius):
        super().__init__()
        self.center = center
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius <= 0:
            raise Exception('Radius should be positive!')
        self.__radius = new_radius

    def area(self):
        return pi*self.radius**2

    def type_name(self):
        return 'Circle'

    def description(self):
        return 'all the dots in a distance of radius from the center'


class Rectangle(FillableShape):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def type_name(self):
        return 'Rectangle'

    def description(self):
        return 'defined by two dots on opposite sides of one diagonal'


if __name__ == "__main__":
    shape = Shape()
    print("Shape type: %s" % (shape.type_name()))
    print("Shape description: %s" % (shape.description()))
    print("Shape full desc: %s" % (shape.full_description()))
    print("Shape name: %s" % (shape.name))
    shape.name = 'My first abstract shape'
    print("Shape name: %s" % (shape.name))
    shape.line_color = 'red'
    print("Shape line color: %s" % (shape.line_color))
    shape = StraightLine([-1, -1], [1, 1])
    print("Shape type: %s" % (shape.type_name()))
    print("Shape description: %s" % (shape.description()))
    print("Shape full desc: %s" % (shape.full_description()))
    print("Shape line color: %s" % (shape.line_color))
    shape.line_color = 'orange'
    print("Shape line color: %s" % (shape.line_color))
    shape = BrokenLine([[1, 1], [3, 3], [3, 2], [2, 3], [3, 3]])
    print("Shape type: %s" % (shape.type_name()))
    print("Shape description: %s" % (shape.description()))
    print("Shape full desc: %s" % (shape.full_description()))
    shape.line_color = 'yellow'
    print("Shape line color: %s" % (shape.line_color))
    shape = FillableShape()
    print("Shape type: %s" % (shape.type_name()))
    print("Shape description: %s" % (shape.description()))
    print("Shape full desc: %s" % (shape.full_description()))
    print("Shape line color: %s" % (shape.line_color))
    shape.line_color = 'orange'
    print("Shape line color: %s" % (shape.line_color))
    print("Shape fill color: %s" % (shape.fill_color))
    shape.fill_color = 'yellow'
    print("Shape fill color: %s" % (shape.fill_color))
    shape = Circle([0, 0], 1)
    print("Shape type: %s" % (shape.type_name()))
    print("Shape description: %s" % (shape.description()))
    print("Shape full desc: %s" % (shape.full_description()))
    print("Shape radius: %s" % (shape.radius))
    print("Shape area: %s" % (shape.area()))
    shape.line_color = 'green'
    print("Shape line color: %s" % (shape.line_color))
    shape.fill_color = 'blue'
    print("Shape fill color: %s" % (shape.fill_color))
    try:
        shape.radius = -1
    except Exception as e:
        print('EXCEPTION:', e)
    shape = Rectangle([-1, -1], [1, 1])
    print("Shape type: %s" % (shape.type_name()))
    print("Shape description: %s" % (shape.description()))
    print("Shape full desc: %s" % (shape.full_description()))
    print("Shape line color: %s" % (shape.line_color))
    shape.line_color = 'navy'
    print("Shape line color: %s" % (shape.line_color))
    print("Shape fill color: %s" % (shape.fill_color))
    shape.fill_color = 'purple'
    print("Shape fill color: %s" % (shape.fill_color))
