#!/usr/bin/python3
"""8-rectangle.py
This module contains a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py).
Instantiation with width and height: def __init__(self, width, height):
    - width and height must be private. No getter or setter
    - width and height must be positive integers,
        validated by integer_validator
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle"""

    def __init__(self, width, height):
        """Iniatilizes a Rectangle object when it is instanciated
        Args:
            width (int): Width of rectangle
            height (int): Height of rectangle
        """
        super().__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
