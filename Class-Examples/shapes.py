#!/usr/bin/env python


class Square:
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return 'Square({0})'.format(self.length)

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return self.length * 4


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return 'Rectangle({0} by {1})'.format(self.length, self.width)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * 2 + self.width * 2


if __name__ == '__main__':
    shapes = [Square(3), Rectangle(3, 2)]

    for s in shapes:
        print s
        print '  area:', s.area()
        print '  perimeter:', s.perimeter()
        
