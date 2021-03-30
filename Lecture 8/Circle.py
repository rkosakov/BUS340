from math import pi
class Circle:
    def __init__(self, radius = 1):
        self.__radius = radius
    
    def getParameter(self):
        return 2 * self.__radius + pi
    
    def getArea(self):
        return self.__radius * self.__radius * pi

    def setRadius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            self.__radius = 1

    def getRadius(self):
        return self.__radius 
        