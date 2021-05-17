# making the classes, Rectangle and Square.
# define 'calculate_permission method' to calculate perimeters of the shapes and return. 
# meke the objects, Rectangle and Square, call the each calculate_perimeter methods.
# define change_size method at Square method.
# conduct decrement(when minus value) or increment of Square object's width only that amount of the passed value.

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return (self.width + self.length) * 2
        
class Square():
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, new_size):
        self.side += new_size

rectangle = Rectangle(20, 300)
print(rectangle.calculate_perimeter())

square = Square(4)
print(square.calculate_perimeter())

print(square.side)
square.change_size(200)
print(square.side)
square.change_size(-144)
print(square.side)


# define Shape class.
# define 'what_am_i' method returning "I am a shape" whrn called.
# change the before class, Rectagle and Square, make inheritanced this Shape class.
# make the objects, Rectabgle and Square, and call the added method 'what_am_i' by this challenge.

class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return (self.width + self.length) * 2
      
class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4


rectangle2 = Rectangle(29, 46)
square2 = Square(34)

rectangle2.what_am_i()
print(rectangle2.calculate_perimeter())
square2.what_am_i()
print(square2.calculate_perimeter())


# define the classes, Horse and Rider.
# make Horse providing to Rider by using composition.

class Horse:
    def __init__(self, name, breed, color, jockey):
        self.name = name
        self.breed = breed
        self.color = color
        self.jockey = jockey

class Rider:
    def __init__(self, name):
        self.name = name

M_Demuro = Rider("Mirco Demuro")
Kitasan = Horse("KitasanBlack", "Thoroughbred", "Bay", M_Demuro)

print("The name of rider is {}.".format(Kitasan.jockey.name))
print("The name of horse is {}, {}, has {} coat color, and {} rided on him.".format(Kitasan.name, Kitasan.breed, Kitasan.color, Kitasan.jockey.name))






