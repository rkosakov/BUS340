from GeometricObject import GeometricObject
import math

class Rectangle(GeometricObject):
    def __init__(self, width = 1, height = 1):
        super().__init__()
        self.__width = width
        self.__height = height
    
    def getWidth(self):
        return self.__width
    
    def setWidth(self, width):
        self.__width = width

    def getHeigth(self):
        return self.__height
    
    def setHeigth(self, heigth):
        self.__height = heigth
    
    def getPerimeter(self):
        return 2 * self.__width + 2 * self.__height
    
    def getArea(self):
        return self.__width * self.__height

    def printRectnagle(self):
        print(self.__str__() + "width: " + str(self.__width) + "height " + str(self.__height))
        
        
