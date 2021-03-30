import math 
from AbstractGeometricObject import GeometricObject

class Circle(GeometricObject):
    def __init__(self, radius = 1): # Construct a circle object
        super().__init__()
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            self.__radius = 1
    
    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi
    
    def getDiameter(self):
        return 2 * self.__radius

    def printCircle(self):
        print(self.__str__() + " radius: " + str(self.__radius))

    # Override the __str__ method defined in GeometricObject
    def __str__(self):
        return super().__str__() + " radius: " + str(self.__radius)