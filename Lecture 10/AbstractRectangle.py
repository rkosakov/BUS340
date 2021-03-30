from AbstractGeometricObject import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self, width = 1, height = 1): # Construct a circle object
        super().__init__()
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        if width > 0:
            self.__width = width
        else:
            self.__width = 1

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        if height > 0:
            self.__height = height
        else:
            self.__height = 1
    
    def getPerimeter(self):
        return 2 * self.__width + 2 * self.__height

    def getArea(self):
        return self.__width * self.__height

    # Override the __str__ method defined in GeometricObject
    def __str__(self):
        return super().__str__() + " widt: " + str(self.__width) + " height: " + str(self.__height)