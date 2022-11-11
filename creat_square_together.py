import turtle

James = turtle.Turtle()  # instatiates object so it can exist name of object is James
John  = turtle.Turtle()
Jacob = turtle.Turtle()
Jerry = turtle.Turtle()


James.color("red")  # sets object color to red so we can keep track of it
John.color("blue")
Jacob.color("green")
Jerry.color("orange")


def basic_square_together():
    James.speed(1)
    John.speed(1)
    Jacob.speed(1)
    Jerry.speed(1)
    James.penup()
    John.penup()
    Jacob.penup()
    Jerry.penup()
    James.lt(90) #bottom left travel up
    #top left travel right
    Jacob.rt(90)  # top right travel down
    Jerry.lt(180) # bottom right travel left
    James.goto(-60,0) # bottom left travel up
    John.goto(-60, 60) #top left travel right
    Jacob.goto(60, 60)#top right travel down
    Jerry.goto(60, 0) #bottom right travel left
    James.showturtle()
    John.showturtle()
    Jacob.showturtle()
    Jerry.showturtle()
    James.pendown()
    John.pendown()
    Jacob.pendown()
    Jerry.pendown()
    Jacob.forward(60)
    Jerry.forward(120)
    James.forward(60)
    John.forward(120)
    turtle.done()



basic_square_together()