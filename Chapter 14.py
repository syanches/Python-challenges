# Задание 1
class Square: 
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self)

    def __repr__(self):
        return "{} на {} на {} на {}".format(self.side, self.side, self.side, self.side)

sq1 = Square(4)
sq2 = Square(34)
sq3 = Square(10)
sq4 = Square(11)

# print(Square.square_list)


# Задание 2

# Задание 3

def equals(self, other):
    return self is other


square1 = Square(1)
square2 = square1
square3 = Square(1)

print(equals(square1, square2))
print(equals(square3, square2))
print(equals(square3, square1))