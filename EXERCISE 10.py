##import turtle
##
##turtle.setup(600, 400)
##wn = turtle.Screen()
##wn.title("Handling Keypresses!")
##wn.bgcolor("lightgreen")
##
##tess = turtle.Turtle()
##a = 3
##tess.pensize(a)
##
##def h1():
##    tess.forward(30)
##
##def h2():
##    tess.left(45)
##
##def h3():
##    tess.right(45)
##
##def h4():
##    wn.bye()
##
##def h5():
##    tess.color("red")
##
##def h6():
##    tess.color("green")
##
##def h7():
##    tess.color("blue")
##
##def h8():
##    global a
##    if a < 20:
##        a +=1
##    tess.pensize(a)
##
##def h9():
##    global a
##    if a > 1:
##        a -=1
##    tess.pensize(a)
##
##def h10():
##    tess
##
##
##wn.onkey(h1, "Up")
##wn.onkey(h2, "Left")
##wn.onkey(h3, "Right")
##wn.onkey(h4, "q")
##wn.onkey(h5, "r")
##wn.onkey(h6, "g")
##wn.onkey(h7, "b")
##wn.onkey(h8, "=")
##wn.onkey(h9, "-")
##
##
##wn.listen()
##wn.mainloop()



##turtle.setup(400, 500)
##wn = turtle.Screen()
##wn.title("How to handle mouse clicks on the window!")
##wn.bgcolor("lightgreen")
##
##tess = turtle.Turtle()
##tess.color("purple")
##tess.pensize(3)
##tess.shape("circle")
##
##def h1(x, y):
##    tess.penup()
##    wn.title("Got a click at {0}, {1}".format(x, y))
##    tess.goto(x, y)
##
##wn.onclick(h1)
##wn.mainloop()


##turtle.setup(400, 500)
##wn = turtle.Screen()
##wn.title("Handling mouse clicks!")
##wn.bgcolor("lightgreen")
##
##tess  = turtle.Turtle()     #Create 2 turtles
##tess.color("purple")
##alex = turtle.Turtle()
##alex.color("blue")
##alex.forward(100)       #move them apart
##
##def handler_tess(x, y):
##    wn.title("Tess clicked at {0}, {1}".format(x, y))
##    tess.left(42)
##    tess.forward(30)
##
##def handler_alex(x, y):
##    wn.title("Alex clicked at {0}, {1}".format(x, y))
##    alex.right(84)
##    alex.forward(50)
##
##tess.onclick(handler_tess)
##alex.onclick(handler_alex)
##
##wn.mainloop()


##turtle.setup(400, 500)
##wn = turtle.Screen()
##wn.title("Using a Timer")
##wn.bgcolor("lightgreen")
##
##tess = turtle.Turtle()
##tess.color("purple")
##tess.pensize(3)
##
##def h1():
##    tess.forward(100)
##    tess.left(56)
##
##wn.ontimer(h1, 2000)
##wn.mainloop()

##turtle.setup(400, 500)
##wn = turtle.Screen()
##wn.title("Using a timer to get events")
##wn.bgcolor("lightgreen")
##
##tess = turtle.Turtle()
##tess.color("purple")
##
##def h1():
##    tess.forward(100)
##    tess.left(56)
##    wn.ontimer(h1, 60)
##
##h1()
##wn.mainloop()



##
##import turtle           # Tess becomes a traffic light.
##
##turtle.setup(400,500)
##wn = turtle.Screen()
##wn.title("Tess becomes a traffic light!")
##wn.bgcolor("lightgreen")
##tess = turtle.Turtle()
##
##
##def draw_housing():
##    """ Draw a nice housing to hold the traffic lights """
##    tess.pensize(3)
##    tess.color("black", "darkgrey")
##    tess.begin_fill()
##    tess.forward(80)
##    tess.left(90)
##    tess.forward(200)
##    tess.circle(40, 180)
##    tess.forward(200)
##    tess.left(90)
##    tess.end_fill()
##
##draw_housing()
##
##tess.penup()
### Position tess onto the place where the green light should be
##tess.forward(40)
##tess.left(90)
##tess.forward(50)
### Turn tess into a big green circle
##tess.shape("circle")
##tess.shapesize(3)
##tess.fillcolor("green")
##
### A traffic light is a kind of state machine with three states,
### Green, Orange, Red.  We number these states  0, 1, 2
### When the machine changes state, we change tess' position and
### her fillcolor.
##
### This variable holds the current state of the machine
##state_num = 0
##
##
##def advance_state_machine():
##    global state_num
##    if state_num == 0:       # Transition from state 0 to state 1
##        tess.forward(70)
##        tess.fillcolor("orange")
##        state_num = 1
##    elif state_num == 1:     # Transition from state 1 to state 2
##        tess.forward(70)
##        tess.fillcolor("red")
##        state_num = 2
##    else:                    # Transition from state 2 to state 0
##        tess.back(140)
##        tess.fillcolor("green")
##        state_num = 0
##    wn.ontimer(advance_state_machine, 5000)
##    # Bind the event handler to the space key(Now a timer).
##
##advance_state_machine()
##
###wn.listen()                      # Listen for events
##wn.mainloop()


##import turtle
##
##turtle.setup(400, 500)
##wn = turtle.Screen()
##wn.title("Bash makes a Traffic Light")
##wn.bgcolor("lightgreen")
##
##ola = turtle.Turtle()
##bash = turtle.Turtle()
##qud = turtle.Turtle()
##
##def draw_housing():
##    ola.pensize(3)
##    ola.color("black", "darkgrey")
##    ola.begin_fill()
##    ola.forward(80)
##    ola.left(90)
##    ola.forward(200)
##    ola.circle(40, 180)
##    ola.forward(200)
##    ola.left(90)
##    ola.end_fill()
##
##draw_housing()
##
##ola.hideturtle()
##ola.penup()
##ola.forward(40)
##ola.left(90)
##ola.forward(5)
##ola.right(90)
##ola.pendown()
##ola.pensize(2)
##ola.circle(32)
##ola.penup()
##ola.left(90)
##ola.forward(32)
##ola.shape("circle")
##ola.shapesize(3)
##ola.color("green")
##bash.hideturtle()
##bash.penup()
##bash.forward(40)
##bash.left(90)
##bash.forward(75)
##bash.right(90)
##bash.pendown()
##bash.pensize(2)
##bash.circle(32)
##bash.penup()
##bash.left(90)
##bash.forward(32)
##bash.shape("circle")
##bash.shapesize(3)
##bash.color("yellow")
##qud.hideturtle()
##qud.penup()
##qud.forward(40)
##qud.left(90)
##qud.forward(150)
##qud.right(90)
##qud.pendown()
##qud.pensize(2)
##qud.circle(32)
##qud.penup()
##qud.left(90)
##qud.forward(32)
##qud.shape("circle")
##qud.shapesize(3)
##qud.color("red")
##
##
##state_num = 0
##
##def advance_state_machine():
##    global state_num
##    if state_num == 0:
##        qud.hideturtle()
##        ola.showturtle()
##        state_num = 1
##        wn.ontimer(advance_state_machine, 3000)
##    elif state_num == 1:
##        bash.showturtle()
##        state_num = 2
##        wn.ontimer(advance_state_machine, 1000)
##    elif state_numy == 2:
##        ola.hideturtle()
##        state_num = 3
##        wn.ontimer(advance_state_machine, 1000)
##    else:
##        bash.hideturtle()
##        qud.showturtle()
##        state_num = 0
##        wn.ontimer(advance_state_machine, 2000)
##
##advance_state_machine()
##
##wn.mainloop()



