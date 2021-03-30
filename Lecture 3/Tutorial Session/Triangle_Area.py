import turtle
import math

x1, y1 = eval(input('Enter the cordibates of the first point seperated by a comma: '))
x2, y2 = eval(input('Enter the cordibates of the second point seperated by a comma: '))
x3, y3 = eval(input('Enter the cordibates of the third point seperated by a comma: '))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y2)
turtle.goto(x3, y3)
turtle.goto(x1, y1)

side1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
side2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
side3 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

turtle.penup()
turtle.goto(0, -200)
turtle.write('The area of the triangle is '+ format(area, '0.1f'), align = 'center', font = ('Arial', 12, 'normal'))

turtle.goto(x1, y1)
turtle.write(f'p1 ({x1}, {y1})')
turtle.goto(x2, y2)
turtle.write(f'p2 ({x2}, {y2})')
turtle.goto(x3, y3)
turtle.write(f'p3 ({x3}, {y3})')

turtle.hideturtle()
turtle.done()