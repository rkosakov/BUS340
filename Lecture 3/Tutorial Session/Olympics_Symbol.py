import turtle, math

radius = eval(input('Enter the radius of a circle: '))
separation = 20

turtle.pensize(10)

turtle.penup()
turtle.goto(-radius - separation, radius / 2)

turtle.pendown()
turtle.left(90)
turtle.color('blue')
turtle.circle(radius)

turtle.penup()
turtle.goto(radius, radius / 2)

turtle.pendown()
turtle.color('black')
turtle.circle(radius)

turtle.penup()
turtle.goto(3 * radius + separation, radius / 2)

turtle.pendown()
turtle.color('red')
turtle.circle(radius)

turtle.penup()
turtle.goto(-separation / 2, -radius / 2)

turtle.pendown()
turtle.color('yellow')
turtle.circle(radius)

turtle.penup()
turtle.goto(2 * radius + separation / 2, -radius / 2)

turtle.pendown()
turtle.color('green')
turtle.circle(radius)

turtle.hideturtle()
turtle.done()