import turtle

radius = eval(input('Enter the radius for the face: '))

turtle.color('black')

turtle.penup()
turtle.goto(0, -radius)
turtle.pendown()
turtle.begin_fill()
turtle.color('yellow')
turtle.circle(radius)
turtle.end_fill()

turtle.penup()
turtle.goto(-radius / 3, radius / 6)
turtle.pendown()
turtle.begin_fill()
turtle.circle(radius / 10)
turtle.end_fill()

turtle.penup()
turtle.goto(radius / 3, radius / 6)
turtle.pendown()
turtle.begin_fill()
turtle.circle(radius / 10)
turtle.end_fill()

turtle.penup()
turtle.goto(-radius / 2, -radius / 2)
turtle.setheading(-30)
turtle.pendown()
turtle.circle(radius, 60)

turtle.penup()
turtle.goto(0, -radius / 4)
turtle.setheading(125)
turtle.pendown()
turtle.forward(radius / 6)
turtle.goto(0, -radius / 4)
turtle.setheading(45)
turtle.forward(radius / 6)
turtle.done()