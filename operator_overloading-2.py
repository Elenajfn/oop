import math


# Problem 1
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


# Problem 2
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __gt__(self, other):
        return self.age > other.age


# Problem 4
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


# Problem 5
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius


# Problem 6
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        return self.distance() < other.distance()

    def __gt__(self, other):
        return self.distance() > other.distance()

    def __eq__(self, other):
        return self.distance() == other.distance()

    def __ne__(self, other):
        return self.distance() != other.distance()

    def __ge__(self, other):
        return self.distance() >= other.distance()

    def __le__(self, other):
        return self.distance() <= other.distance()


# Problem 7
class Matrix:
    def __init__(self, data):
        self.data = data  # list of rows

    def __mul__(self, other):
        # columns of the first must equal rows of the second
        if len(self.data[0]) != len(other.data):
            raise ValueError("Matrices cannot be multiplied")
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(other.data[0])):
                total = 0
                for k in range(len(other.data)):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)
            result.append(row)
        return Matrix(result)

    def __str__(self):
        return "\n".join(str(row) for row in self.data)


if __name__ == "__main__":
    print(ComplexNumber(1, 2) + ComplexNumber(3, 4))
    print(ComplexNumber(5, 6) - ComplexNumber(2, 3))
    print(Person("Ana", 30, "F") > Person("Bob", 25, "M"))
    print(Vector(1, 2, 3) * Vector(4, 5, 6))
    c1, c2 = Circle(2), Circle(3)
    print(c1 < c2, c1 > c2, c1 == c2, c1 != c2, c1 >= c2, c1 <= c2)
    p1, p2 = Point(3, 4), Point(1, 1)
    print(p1 < p2, p1 > p2, p1 == p2, p1 != p2, p1 >= p2, p1 <= p2)
    print(Matrix([[1, 2], [3, 4]]) * Matrix([[5, 6], [7, 8]]))
