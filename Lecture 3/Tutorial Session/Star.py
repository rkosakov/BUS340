import turtle

starSize = eval(input('Enter the size of the star: '))
cir = ['red', 'green', 'blue', 'yellow', 'purple']

turtle.pensize(4)
turtle.pencolor('black')

turtle.penup()
turtle.setpos(-90, 30)
turtle.pendown()

turtle.pencolor(cir[0])
turtle.forward(starSize)
turtle.right(144)

turtle.pencolor(cir[1])
turtle.forward(200)
turtle.right(144)

turtle.pencolor(cir[2])
turtle.forward(starSize)
turtle.right(144)

turtle.pencolor(cir[3])
turtle.forward(starSize)
turtle.right(144)

turtle.pencolor(cir[4])
turtle.forward(starSize)
turtle.right(144)

turtle.hideturtle()
turtle.done()
