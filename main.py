from turtle import *
import turtle
import math
from tkinter import messagebox

James = turtle.Turtle()  # instatiates object so it can exist name of object is James
John  = turtle.Turtle()
Jacob = turtle.Turtle()
Jerry = turtle.Turtle()

James.color("red")  # sets object color to red so we can keep track of it
John.color("blue")
Jacob.color("green")
Jerry.color("orange")
James.hideturtle()
John.hideturtle()
Jacob.hideturtle()
Jerry.hideturtle()
#James.speed(0)
counter = 0


def basic_loop_flower():
    James.reset()
    localcounter = 0
    while localcounter <= 10:
        James.begin_fill()
        James.circle(200-localcounter, 100)
        James.lt(90)  # turns turtle left by specified amount default in degrees
        James.circle(200-localcounter, 100)
        James.rt(60)
        James.end_fill()
        if localcounter == 10:  # condition to get to the break statement
            messagebox.showinfo("", "if case has occured")
            James.clear()
            turtle.done()
            break  # stops the loop "breaks out of it"
        else:     # else as a default case
            localcounter = localcounter + 1
           # messagebox.showinfo("", "counter is equal to" + str(counter))



def basic_loop_with_alternating_color():  # use of an if statement to change colors
    James.reset()
    localcounter = 0
    while localcounter <= 10:
        if localcounter % 2 == 0:  # if counter modulo 2 equals 0 then change value
            James.color("blue")
        if localcounter % 2 == 1:
            James.color("red")
            James.circle(200 - localcounter * 2, 100)
            James.lt(100)  # turns turtle left by specified amount default in degrees
            James.circle(200 - localcounter * 5, 100)
            James.rt(100)  # turns turtle right by specified amount default in degrees
        if localcounter == 10:  # condition to get to the break statement
            turtle.done()
            break  # stops the loop "breaks out of it"
        else:  # else as a default case
            localcounter = localcounter + 1
            messagebox.showinfo("", "counter is equal to" + str(localcounter))
def basic_square():
    James.reset()
    James.lt(90)
    James.forward(100)
    James.lt(90)
    James.forward(100)
    James.lt(90)
    James.forward(100)
    James.lt(90)
    James.forward(100)
    James.hideturtle()

    turtle.done()
    return()
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
    James.goto(-20,0) # bottom left travel up
    John.goto(-20, 20) #top left travel right
    Jacob.goto(20, 20)#top right travel down
    Jerry.goto(20, 0) #bottom right travel left
    James.showturtle()
    John.showturtle()
    Jacob.showturtle()
    Jerry.showturtle()
    turtle.done()
def basic_set_position( x ):
    if x == 2:
     James.reset()
     John.reset()
     Jacob.reset()
     Jerry.reset()
    if x == 1:
        James.showturtle()
        John.showturtle()
        Jacob.showturtle()
        Jerry.showturtle()
    James.speed(1)
    John.speed(1)
    Jacob.speed(1)
    Jerry.speed(1)
  #  James.hideturtle()
    James.penup()
    John.penup()
    Jacob.penup()
    Jerry.penup()
    James.lt(90)
    John.lt(90)
    Jacob.lt(90)
    Jerry.lt(90)
    James.goto(20,10)
    John.goto(0,10)
    Jacob.goto(-20,10)
    Jerry.goto(-40,10)
  # James.showturtle()
    if x == 0:
     turtle.done()


def basic_race():
    x=1 # notifys set position that basic race is utilizing it so it doesnt show done
    basic_set_position(x)
    James.speed(2)
    John.speed(3)
    Jacob.speed(4)
    Jerry.speed(5)
    James.forward(100)
    John.forward(100)
    Jacob.forward(100) 
    Jerry.forward(100)





#basic_loop_flower()
#basic_loop_with_alternating_color()
#basic_square()
# basic_set_position()
# basic_race()

basic_square_together()