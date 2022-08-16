import math

#Задание 1

class Apple:
    def __init__(self, size, color, smell, count):
        self.size = size
        self.color = color
        self.smell = smell
        self.count = count

#Задание 2

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2 * math.pi

circ = Circle(3)
print(circ.area())

#Задание 3

class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def area(self):
        return 0.5 * self.a * self.b

tri = Triangle(10, 9)
print(tri.area())

#Задание 4

class Hexagon:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def calculate_perimeter(self):
        return self.a + self.b + self.c + self.d + self.e + self.f

hex = Hexagon(1,45,2,54,6,1)
print(hex.calculate_perimeter())
    
    