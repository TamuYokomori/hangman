# program a Apple class has four attributes with instance variants

class Apple:
    def __init__(self, w, c, d, t):
        self.weight = w
        self.color = c
        self.days = d
        self.temperature = t
        self.mold = d * t

apple = Apple(200, "greenery red", 10, 34)
print(apple)
print(apple.weight)
print(apple.color)
print(apple.days)
print(apple.temperature)
print(apple.mold)


# define Circle class indicating circle.
# the class has area method returning calculated acreage.
# culculating is used pi constant in math built-in　module.
# next, write Circle object, call for area method, output results.

import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * math.pi

circle1 = Circle(23)
print(circle1.calculate_area())


# define Triangle class having area method returining acreage.
# make triangle object, call for area method, output result.

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height / 2

triangle1 = Triangle(293, 548)
print(triangle1.base)
print(triangle1.height)
print(triangle1.area())


# define Hexagon class indicating hexagon.
# in the class, a 'calculate_perimeter' is defined as a method returning calculated length of circumference.
# make hexagon object, call for calculat_perimeter method, return the result.

class Hexagon():
    def __init__(self, one_side_len):
        self.len = one_side_len

    def calculate_perimeter(self):
        return self.len * 6

hexagon1 = Hexagon(33)
print(hexagon1.len)
print(hexagon1.calculate_perimeter())

