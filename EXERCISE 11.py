##a_list = [(),(),()]
##g ='10'
##a_list[0:0] = g
##print((a_list))
##del a_list[2:6]
##print(a_list)
##
##a_list.append(56)
##print(a_list)
##a_list.extend([56, 455, "fdf", "567h"])
##print(a_list)

##def primes_lessthan(n):
##    """ Return a list of all prime numbers less than n. """
##    result = []
##    for i in range(2, n):
##        if is_prime(i):
##           result.append(i)
##    return result

##def is_prime(x):
##    if x >=  2:
##        for i in range(2, x):
##            if x % i == 0:
##                return False
##        return True
##    else:
##        return False
##

##song = "The rain in Spain..."
##wds = song.split()
##print(" ".join(wds))

##a = 4
##b = 6
##temp = a
##a = b
##b = temp

##(a, b) = (4, 6)
##print(a)
##print(b)


##fruit = ["banana", "apple", "quince"]
##
##fruit[1:3] = ("mango", "cucumber")
##print(fruit)

##a = ["banana", "apple", "mango"]
##b = ["banana", "apple", "mango"]
##print(b is a)
##print(type(a))
##print(type(b))
##c = b[:]  #why does cloning a list make the new list b, a one element list with the clone a sublist?
##c[0] = "carrot"
##print(c)
##print(b)

##xs = [1, 2, 3, 4, 5]
##
###for (a, b) in enumerate(xs):
###    print(a, b)
##
##xs.append([5, 9, 3])
##print(xs)

##xs = "seasoning is an important element in cooking".split("i")
##print(xs)


##c = range(10)
##print(c)
##print(list(range(0, 10, 2)))


##import turtle
##tess = turtle.Turtle()
##alex = turtle.Turtle()
##alex.color("hotpink")
##print(alex is tess)


##a = [1, 2, 3]
##b = a[:]
##b[0] = 5


##this = ["I", "am", "not", "a", "crook"]
##that = ["I", "am", "not", "a", "crook"]
##print("Test 1: {0}".format(this is that))
##that = this
##print("Test 2: {0}".format(this is that))


##def swap(x, y):      # Incorrect version
##     print("before swap statement: x:", x, "y:", y)
##     (x, y) = (y, x)
##     print("after swap statement: x:", x, "y:", y)
##     return (x, y)  #fix 1
##
##a = ["This", "is", "fun"]
##b = [2,3,4]
##print("before swap function call: a:", a, "b:", b)
##c = swap(a, b)
##(a, b) = c  #fix 2
##print("after swap function call: a:", a, "b:", b)