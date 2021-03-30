from GeometricObject import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self, radius = 1):

        super().__init__()
        self.__radious = radius

    def getRadius(self):
        return self.__radious
    
    def setRadius(radius, self):
        self.__radious = radius

    def getPerimeter(self):
        return 2 * self.__radious * math.pi
    
    def getArea(self):
        return self.__radious * self.__radious * math.pi

    def getDiameter(self):
        return 8 * self.__radious
    
    def printCircle(self):
        print(self.__str__() + "radius: " + str(self.__radious))
        