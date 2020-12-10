import math
class Shape:
    def __init__(self, colour="green", filled=True):
        self.colour = colour
        self.filled = filled

    def getColour(self):
        return self.colour

    def setColour(self, col):
        self.colour = col

    def isFilled(self):
        if self.colour == "":
            self.filled = False
            return self.filled

        else:
            return self.filled

    def setFilled(self, fill):
        self.filled = fill

    def toString(self):
        if self.filled == True:
            return f"A shape with colour of {self.colour} and filled"
        else:
            return f"A shape with colour of {self.colour} and not filled"

def testShape():
    print("this is a test for Shape")
    triangle = Shape('green')
    print(triangle.getColour())
    print(triangle.isFilled())
    triangle.setColour("skyblue")
    triangle.setFilled(False)
    print(triangle.getColour())
    print(triangle.isFilled())

class Circle(Shape):
    def __init__(self, colour="green", filled=True, radius=1.0):
        super().__init__(colour, filled)
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, rad):
        self.radius = rad

    def getArea(self):
        return math.pi * self.radius ** 2

    def getPerimeter(self):
        return math.pi * self.radius * 2

    def toString(self):
        return f"A circle with radius = {self.radius}, which is a subclass of {super().toString()}"

def testCircle():
    circle = Circle()



class Rectangle(Shape):
    def __init__(self, colour="green", filled=True, width=1.0, length=2.0):
        super().__init__(colour, filled)
        self.width = width
        self.length = length

    def getWidth(self):
        return self.width

    def setWidth(self, new_width):
        self.width = new_width

    def getLength(self):
        return self.length

    def setLength(self, new_length):
        self.length = new_length

    def getArea(self):
        return self.width * self.length

    def getPerimeter(self):
        return 2 * (self.width + self.length)

    def toString(self):
        return f"A rectangle with width = {self.width} and length = {self.length} which is a subclass of " \
               f"{super().toString}"

def testRectangle():
    print("this is the test for rectangle:")
    rectangle = Rectangle()
    print(rectangle.getColour())
    print(rectangle.getArea())
    print(rectangle.getPerimeter())


class Square(Rectangle):
    def __init__(self, colour="green", filled=True, width=1.0, length=1.0):
        super().__init__(colour, filled, width, length)
        if self.length != self.length:
            self.length = self.width

    def getSide(self):
        return self.width

    def setSide(self, side):
        self.width = side
        self.length = side

    def setLength(self, side):
        self.length = side
        self.width = side

    def setWidth(self, side):
        self.width = side
        self.length = side

    def toString(self):
        return f"A square with side = {self.length}, which is a subclass of {super(Rectangle).toString()}"

def testSquare():
    print("This is the square object testing")
    square = Square()
    print(square.getSide())
    square.setSide(4.0)
    print(square.getSide())
    print(square.getArea())
    print(square.getPerimeter())

if __name__ == "__main__":
    testShape()
    testCircle()
    testRectangle()
    testSquare()

