# Задание 1

class Shape:
    def what_am_i(self):
        print("I am shape")

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_perimeter(self):
        return self.a * 2 + self.b * 2   

    def what_am_i(self):
        print("I am rectangle")     


class Square(Shape): 
    def __init__(self, a):
        self.a = a

    def calculate_perimeter(self):
        return self.a * 4

    def change_size(self, a):
        self.a += a

    def what_am_i(self):
        print("I am square")

rect = Rectangle(4, 10)
print(rect.calculate_perimeter())
sq = Square(10)
print(sq.calculate_perimeter())

sq.change_size(-4)
print(sq.calculate_perimeter())


sq.what_am_i()
rect.what_am_i()

# Задание 2

# Задание 3


# Задание 4



class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider 

class Rider:
    def __init__(self, name):
        self.name = name

rider = Rider("Artem")

horse = Horse("Bior", rider)

print(horse.rider.name)
