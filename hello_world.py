#print('Hello, world')
#user_name=input('Enter your name: ')
#print('Hello', user_name)

#print('The area is: ', 3.14159* float(input('What is the radius'))**2)


#total_seconds = int(input('How many seconds, in total?'))
#total_hours = total_seconds // 3600
#total_seconds_remaining = total_seconds % 3600
#total_minutes = total_seconds_remaining // 60
#total_final_seconds = total_seconds_remaining % 60
#print('Hours = ', total_hours, 'Minutes =', total_minutes, 'Seconds =', total_final_seconds)


##a = 'All '
##b = 'work '
##c = 'and '
##d = 'no '
##e = 'play '
##f = 'makes '
##g = 'jack '
##h = 'a '
##i = 'dull '
##h = 'boy'
##
##print(a + b + c + d + e + f + g + h )

##print(6 * 1 -2)
##print(6 * (1 - 2))

##bruce = 6
##print(bruce + 4)

##p = 10000
##n = 12
##r = 0.08
##t = int(input('What is the duration of the interest?'))
##a = p*(1 + r/n)**(n*t)
##print(a)

##print(12%15)

##time_now = int(input('What is the time now? (in hrs)'))
##alarm_duration = int(input('in how long do you want to reminded (hrs)'))
##time = time_now + alarm_duration
##time_now = time % 24
##print(time_now)


##import turtle
##wn = turtle.Screen()
##alex = turtle.Turtle()
##alex.color("red")
##alex.forward(50)
##alex.left(90)
##alex.forward(30)
##wn.mainloop()

##import turtle
##wn = turtle.Screen()
##wn.bgcolor(input("Select background color"))
##wn.title('Hello, Bash')
##
##bash = turtle.Turtle()
##bash.color(input("Select pen color"))
##bash.pensize(int(input('Specify pen size')))
##
##bash.forward(50)
##bash.left(30)
##bash.forward(50)
##
##wn.mainloop()


##import turtle
##wn = turtle.Screen()
##wn.bgcolor("lightgreen")
##wn.title("The Three Musketeers")
##
##bash = turtle.Turtle()
##bash.color("lightblue")
##bash.pensize(3)
##
##qudus = turtle.Turtle()
##qudus.color("Black")
##qudus.pensize(3)
##
##ola =turtle.Turtle()
##ola.color("red")
##ola.pensize(3)
##
##bash.forward(100)
##bash.left(120)
##bash.forward(50)
##bash.left(300)
##bash.forward(50)

##wn.mainloop()


##import turtle
##__import__("turtle").__traceable__ = False
##def draw_multicolor_square(t, sz):
##    """Make turtle t draw multicolor squares"""
##    for i in ["red", "purple", "hotpink", "blue"]:
##        t.color(i)
##        t.forward(sz)
##        t.left(90)
##
##wn = turtle.Screen() #Set up window and attributes
##wn.bgcolor("lightgreen")
##
##bash = turtle.Turtle() #Create turtle and attributes
##bash.pensize(4)
##
##size = 20   #size of smallest square
##for i in range(15):
##    draw_multicolor_square(bash, size)
##    size = size +10     #increase size of square
##    bash.forward(10)    #Move bash forward a little
##    bash.right(18)      #Turn bash right a little
##
##wn.mainloop()

##def distance(x1, y1, x2, y2):
##    dx = x2 - x1
##    dy = y2 - y1
##    dsquared = dx*dx + dy*dy
##    result = dsquared**0.5
##    return result
##
##distance(1, 2, 4, 6)

##import sys
##
##def test(did_pass):
##    """  Print the result of a test.  """
##    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
##    if did_pass:
##        msg = "Test at line {0} ok.".format(linenum)
##    else:
##        msg = ("Test at line {0} FAILED.".format(linenum))
##    print(msg)
##
##
##def absolute_value(x):
##    if x < 0:
##        return -x
##    else:
##        return 1
##
##
##def test_suite():
##    """ Run the suite of tests for code in this module (this file).
##    """
##    test(absolute_value(17) == 17)
##    test(absolute_value(-17) == 17)
##    test(absolute_value(0) == 0)
##    test(absolute_value(3.14) == 3.14)
##    test(absolute_value(-3.14) == 3.14)
##
##test_suite()        # Here is the call to run the tests





