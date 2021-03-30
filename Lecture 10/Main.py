from AbstractCircle import Circle
from AbstractRectangle import Rectangle


def equalArea(o1, o2):
    return o1.getArea() == o2.getArea()

def displayGeometricObject(o):
    print()
    print(o)
    print("The area is " + str(o.getArea()))
    print("The perimeter is " + str(o.getPerimeter()))

def main():
    geo1 = Circle(2.0)
    geo2 = Rectangle(6, 4)

    print("The two objects have the same area?" + str(equalArea(geo1, geo2)))
    displayGeometricObject(geo1)
    displayGeometricObject(geo2)

    list = [Circle(2.0), Circle(3.0), Rectangle(5.0, 3.0), Rectangle(4.0, 6.0)]

    for obj in list:
        print("The two objects have the same area?" + str(equalArea(geo1, obj)))
    
    for obj in list:
        print("The two objects have the same area?" + str(equalArea(geo2, obj)))

        

main() 