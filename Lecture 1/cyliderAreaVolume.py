from math import pi, pow

radius = float(input('Enter the radius for the cylinder: '))
len = float(input('Enter the length for the cylinder: '))

area = pow(radius, 2) * pi
volume = area * len

print(f'The radius of the Cylinder is: {radius}')
print(f'The length of the Cylinder is: {len}')
print(f'The area of the Cylinder is: {area:.2f}')
print(f'The volume of the Cylinder is: {volume:.2f}')