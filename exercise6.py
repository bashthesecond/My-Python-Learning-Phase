#-------------------------------------------------------------------------------
### Name:        exercise
### Purpose:
###
### Author:      Q.O Bashiru
###
### Created:     22/06/2020
### Copyright:   (c) Q.O Bashiru 2020
### Licence:     <your licence>
###-------------------------------------------------------------------------------
##
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
##def turn_clockwise(x):
##    if x == "N":
##        return "E"
##    elif x == "E":
##        return "S"
##    elif x == "S":
##        return "W"
##    elif x == "W":
##        return "N"
##
##
##def day_name(k):
##    if k == 0:
##        return "Sunday"
##    elif k == 1:
##        return "Monday"
##    elif k == 2:
##        return "Tuesday"
##    elif k == 3:
##        return "Wednesday"
##    elif k == 4:
##        return "Thursday"
##    elif k == 5:
##        return "Friday"
##    elif k == 6:
##        return "Saturday"
##
##
##def day_num(k):
##    if k == "Sunday":
##        return 0
##    elif k == "Monday":
##        return 1
##    elif k == "Tuesday":
##        return 2
##    elif k == "Wednesday":
##        return 3
##    elif k == "Thursday":
##        return 4
##    elif k == "Friday":
##        return 5
##    elif k == "Saturday":
##        return 6
##
##
##def day_add(day, no_days_hol):
##    no = day_num(day)
##    if no_days_hol >= 0:
##        no_day_week = (no_days_hol + no) % 7
##        return day_name(no_day_week)
##    if no_days_hol < 0:
##        no_day_week = no - ((-no_days_hol) % 7)
##        if no_day_week < 0:
##            return day_name(no_day_week + 7)
##        elif no_day_week >= 0:
##            return day_name(no_day_week)
##
##
##def days_in_month(k):
##    if k == "January" or k == "March" or k == "May" or k == "July" or k == "August" or k == "October" or k == "December":
##        return 31
##    elif k == "September" or k == "April" or k == "June" or k == "November":
##        return 30
##    elif k == "February":
##        return 28
##
##
##def to_secs(k, l, m):
##    return int((k * 3600) + (l * 60) + m)
##
##
##def hours_in(k):
##    return int(k // 3600)
##
##
##def minutes_in(k):
##    return int((k % 3600) / 60)
##
##
##def seconds_in(k):
##    return int((k % 3600) % 60)
##
##
##def slope(x1, y1, x2, y2):
##    return (y2 - y1) / (x2 - x1)
##
##
##def intercept(x1, y1, x2, y2):
##    return y2 - (slope(x1, y1, x2, y2) * x2)
##
##
##def is_even(n):
##    return n % 2 == 0
##
##def is_odd(n):
##    return n % 2 != 0
##
##
##def is_factor(f, n):
##    return n % f == 0
##
##def is_multiple(f, n):
##    return f % n == 0
##
##
##def f2c(t):
##    return round((t - 32) * 5 / 9)
##
##
##def c2f(t):
##    return round((t * 9 / 5) + 32)
##
##
##def test_suite():
##    """ Run the suite of tests for code in this module (this file).
##    """
##    test(turn_clockwise("N") == "E")
##    test(turn_clockwise("W") == "N")
##    test(turn_clockwise(42) == None)
##    test(turn_clockwise("rubbish") == None)
##    test(day_name(3) == "Wednesday")
##    test(day_name(6) == "Saturday")
##    test(day_name(42) == None)
##    test(day_num("Friday") == 5)
##    test(day_num("Sunday") == 0)
##    test(day_num(day_name(3)) == 3)
##    test(day_name(day_num("Thursday")) == "Thursday")
##    test(day_num("Halloween") == None)
##    test(day_add("Monday", 4) ==  "Friday")
##    test(day_add("Tuesday", 0) == "Tuesday")
##    test(day_add("Tuesday", 14) == "Tuesday")
##    test(day_add("Sunday", 100) == "Tuesday")
##    test(day_add("Sunday", -1) == "Saturday")
##    test(day_add("Sunday", -7) == "Sunday")
##    test(day_add("Tuesday", -100) == "Sunday")
##    test(days_in_month("February") == 28)
##    test(days_in_month("December") == 31)
##    test(to_secs(2, 30, 10) == 9010)
##    test(to_secs(2, 0, 0) == 7200)
##    test(to_secs(0, 2, 0) == 120)
##    test(to_secs(0, 0, 42) == 42)
##    test(to_secs(0, -10, 10) == -590)
##    test(to_secs(2.5, 0, 10.71) == 9010)
##    test(to_secs(2.433,0,0) == 8758)
##    test(hours_in(9010) == 2)
##    test(minutes_in(9010) == 30)
##    test(seconds_in(9010) == 10)
##    test(slope(5, 3, 4, 2) == 1.0)
##    test(slope(1, 2, 3, 2) == 0.0)
##    test(slope(1, 2, 3, 3) == 0.5)
##    test(slope(2, 4, 1, 2) == 2.0)
##    test(intercept(1, 6, 3, 12) == 3.0)
##    test(intercept(6, 1, 1, 6) == 7.0)
##    test(intercept(4, 6, 12, 8) == 5.0)
##    test(is_even(1) == False)
##    test(is_even(4) == True)
##    test(is_even(0) == True)
##    test(is_odd(1) == True)
##    test(is_odd(4) == False)
##    test(is_odd(0) == False)
##    test(is_factor(3, 12))
##    test(not is_factor(5, 12))
##    test(is_factor(7, 14))
##    test(not is_factor(7, 15))
##    test(is_factor(1, 15))
##    test(is_factor(15, 15))
##    test(not is_factor(25, 15))
##    test(is_multiple(12, 3))
##    test(is_multiple(12, 4))
##    test(not is_multiple(12, 5))
##    test(is_multiple(12, 6))
##    test(not is_multiple(12, 7))
##    test(f2c(212) == 100)     # Boiling point of water
##    test(f2c(32) == 0)        # Freezing point of water
##    test(f2c(-40) == -40)     # Wow, what an interesting case!
##    test(f2c(36) == 2)
##    test(f2c(37) == 3)
##    test(f2c(38) == 3)
##    test(f2c(39) == 4)
##    test(c2f(0) == 32)
##    test(c2f(100) == 212)
##    test(c2f(-40) == -40)
##    test(c2f(12) == 54)
##    test(c2f(18) == 64)
##    test(c2f(-48) == -54)
##
##test_suite()        # Here is the call to run the tests
##
##test(3 % 4 == 0)
##test(3 % 4 == 3)
##test(3 / 4 == 0)
##test(3 // 4 == 0)
##test(3+4  *  2 == 14)
##test(4-2+2 == 0)
##test(len("hello, world!") == 13)

count =  0
a = str(count)
count +=1
print(a)


