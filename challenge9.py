# add the class variant, square_list, to Square class
# add the obj to the list when made a new obj of Square class

class Square:
    square_class = []

    def __init__(self, s):
        self.side1 = s
        self.side2 = s
        self.side3 = s
        self.side4 = s
        self.square_class.append(self.side1)

    # pass the obj of Square class to print function
    # output the each length of the 4 side
    def print_all_side_length(self):
        print("{} by {} by {} by {}".format(self.side1, self.side2, self.side3, self.side4))

square1 = Square(10)
square2 = Square(29)
square3 = Square(88)

print(Square.square_class)
square1.print_all_side_length()
square2.print_all_side_length()
square3.print_all_side_length()


# write a function recieving 2 parameters.
# this function returns 'True' when passed the same obj, 'False' when not.

class Horse:
    def __init__(self):
        self.name = 'DeepImpact'

DeepImpact = Horse()
same_Horse = DeepImpact
print(DeepImpact is same_Horse)

another_Horse = Horse()
print(DeepImpact is another_Horse)
    
        
