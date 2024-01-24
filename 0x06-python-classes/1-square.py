#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

# Example usage:
if __name__ == "__main__":
    square = Square(5)
    print("Area of the square:", square.area())

