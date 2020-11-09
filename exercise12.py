import random
import time
import seqtools #A test to create our own modules
import math as ma
from unit_tester import test
import string

##
##rng = random.Random(147)
##dice_throw = rng.randrange(1, 7)    #method 1
####delay_in_seconds = rng.random() * 5.0 #method 2
##print(dice_throw)
##dice_throw = rng.randrange(1, 7)    #method 1
##print(dice_throw)


##cards = list(range(52))
##next_card = rng.shuffle(cards)


##def make_random_ints(num, lower_bound, upper_bound):
##    """Generate a list of random numbers between upper bound and lower bound.
##    keeping upper bound open abd lower bound closed.
##    """
##    rng = random.Random()
##    result = []
##    for i in range(num):
##        result.append(rng.randrange(lower_bound, upper_bound))
##    return result
##
##
##print(make_random_ints(5, 1, 13))  # Pick 5 random month numbers

##def make_random_nonrepetitive_ints(num, lower_bound, upper_bound):
##    """Generates a list similar to earlier specified, however
##    repetitions are avoided
##    note - not the best method to use here, if range of numbers is a lot
##    """
##    rng = random.Random()
##    xs = list(range(lower_bound, upper_bound))
##    rng.shuffle(xs)
##    result = xs[:5]
##    return result

##def make_random_ints_no_dups(num, lower_bound, upper_bound):
##    """Generate a numbered list of numbers between a specified lower and upper
##    boundary.
##    """
##    result = []
##    rng = random.Random()
##    for i in range(num):
##        while True:
##            candidate = rng.randrange(lower_bound, upper_bound)
##            if candidate not in result:
##                break
##        result.append(candidate)
##    return result
##
####xs = make_random_ints_no_dups(5, 1, 10000000)
####print(xs)
##xs = make_random_ints_no_dups(10, 1, 6)

##def do_my_sum(xs):
##    sum = 0
##    for i in xs:
##        sum += i
##    return sum
##
##sz = 10000000
##testdata = range(sz)
##
##t0 = time.time()
##my_result = do_my_sum(testdata)
##t1 = time.time()
##print("My result = {0} (time taken = {1:4f} seconds)".format(my_result, t1 - t0))
##
##t2 = time.time()
##their_result = sum(testdata)
##t3 = time.time()
##print("Their result = {0} (time taken = {1:4f} seconds)".format(their_result, t3 -t2))
##

##s = "A string!"
##a = seqtools.remove_at(4, s)  #The test of a created module, "seqtools"
##print(a)

##def range(n):
##    return 123*n
##print(range(10))


##n = 10
##m = 3
##def f(n):
##    m = 7
##    return 2*n+m
##print(f(5), n, m)

##
##x = ma.sqrt(9)
##print(x)

##print("exercises")
##print("No 1")

##import calendar
##cal = calendar.TextCalendar(firstweekday = 3)
##cal.pryear(2020)
##cal.prmonth(2020, 6)

##d = calendar.LocaleTextCalendar(6, "YORUBA")
##d.pryear(2012)

##print(calendar.isleap(2020))


##print("No 2")
##import math
##
##print(math.ceil(2.3))
##print(math.floor(2.3))

##print("No 3")
##import copy
##a = [1, 4, 6, 7, 9]
##b = copy.deepcopy(a)
##print(a is b)
##a.append(10)
##print(a)
##print(b)

##def myreplace(old, new, s):
##    """ Replace all occurrences of old with new in s. """
##    ...
##    temp_str = s.split(old)
##    return new.join(temp_str)
##
##
##test(myreplace(",", ";", "this, that, and some other thing") ==
##                         "this; that; and some other thing")
##test(myreplace(" ", "**",
##                 "Words will now be separated by stars.") ==
##                 "Words**will**now**be**separated**by**stars.")


n = [6, 9, 5, 3, 6, 2, 1, 9]
xs = n.sort()
print(xs)


