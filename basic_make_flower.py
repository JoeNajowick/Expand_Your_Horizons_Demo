import turtle
James = turtle.Turtle()  # instatiates object so it can exist name of object is James

James.speed(0)
localcounter = 0
while localcounter <= 10:
    James.begin_fill()
    James.circle(200 - localcounter, 100)
    James.lt(90)  # turns turtle left by specified amount default in degrees
    James.circle(200 - localcounter, 100)
    James.rt(60)
    James.end_fill()
    if localcounter == 10:  # condition to get to the break statement
        turtle.done()
        break  # stops the loop "breaks out of it"
    else:  # else as a default case
        localcounter = localcounter + 1
    # messagebox.showinfo("", "counter is equal to" + str(counter))
