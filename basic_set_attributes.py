from turtle import *
import turtle

James = turtle.Turtle()  # instatiates object so it can exist name of object is James
John  = turtle.Turtle()
Jacob = turtle.Turtle()
Jerry = turtle.Turtle()

James.color("red")  # sets object color to red so we can keep track of it
John.color("blue")
Jacob.color("green")
Jerry.color("orange")

James.speed(1) #sets speed of turtles action or movement
John.speed(2)
Jacob.speed(3)
Jerry.speed(4)
#  James.hideturtle()
James.penup()
John.penup()
Jacob.penup()
Jerry.penup()
James.lt(90) # turns turtle left 90 units
John.lt(90)
Jacob.lt(90)
Jerry.lt(90)
James.goto(20, 10) # sends turtle to new position using an x,y coordinate system
John.goto(0, 10)
Jacob.goto(-20, 10)
Jerry.goto(-40, 10)

turtle.done()