import turtle 

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()

turtle.begin_fill()
turtle.forward(100)
turtle.right(60)

turtle.forward(100)
turtle.right(60)

turtle.forward(100)
turtle.right(60)

turtle.forward(100)
turtle.right(60)

turtle.forward(100)
turtle.right(60)

turtle.forward(100)
turtle.right(60)

turtle.color('red')
turtle.end_fill()

turtle.penup()
turtle.goto(-10, -10)
turtle.pendown()
turtle.color('white')
turtle.write('STOP', font = ('Times', 36, 'bold'))
turtle.hideturtle()

turtle.done()