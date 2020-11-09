import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


##def mysum(k):
##    """Sum of number in a range"""
##    running_sum = 0
##    for i in k:
##        running_sum = running_sum + i
##    return running_sum
##
##
##def sum_to(n):
##    """"Sum of numbers to a value 'n' """
##    ss = 0
##    v = 1
##    while v < n + 1:
##        ss = ss + v
##        v = v + 1
##    return ss
##
##
##def num_zero_and_five_digits(n):
##    """To determine digits that are 0 or 5 in a number"""
##    count = 0
##    while n != 0:
##        if n % 5 == 0 or n % 10 == 0:
##            count = count +1
##        n = n // 10
##    return count
##
##
##
##

##for x in range(13):   # Generate numbers 0 to 12
##    print(x, "\t", 2**x)

##def to_multiply(n):
##    for i in range (1, 13):
##        print(n * i, end = "\t")
##    print()
##
##
##def print_multiplication():
##    for i in range(1, 13):
##        to_multiply(i)

##for i in [12, 16, 17, 24, 29]:
##    if i % 2 == 1:  # If the number is odd
##       break        #  ... immediately exit the loop
##    print(i)
##print("done")

##import random
##rng = random.Random()
##number = rng.randrange(1, 1000)
##
##guesses = 0
##msg = ""
##
##while True:
##    guess = int(input(msg + "\nGuess my number between 1 and 1000: "))
##    guesses += 1
##    if guess < number:
##        msg += str(guess) + "is too low.\n"
##    elif guess > number:
##        msg += str(guess) + "is too high\n"
##    else:
##        break
##input("\nGreat, you got it in " + str(guesses) + "guesses!\n\n")




##def print_multiples(n, high):
##    for i in range(1, high + 1):
##        print(n * i, end="\t")
##    print()
##
##
##def print_mult_table(high):
##    for i in range(1, high + 1):
##        print_multiples(i, high)
##
##
##print_mult_table(7)


##import random                   # We cover random numbers in the
##rng = random.Random()           #  modules chapter, so peek ahead.
##number = rng.randrange(1, 1000) # Get random number between [1 and 1000).
##
##guesses = 0
##msg = ""
##
##while True:
##    guess = int(input(msg + "\nGuess my number between 1 and 1000: "))
##    guesses += 1
##    if guess > number:
##        msg += str(guess) + " is too high.\n"
##    elif guess < number:
##        msg += str(guess) + " is too low.\n"
##    else:
##        break
##
##input("\n\nGreat, you got it in {0} guesses!\n\n".format(guesses))


##celebs = [("Bradd Pitt", 1963), ("Jack Nicholson", 1937), ("Justin Bieber", 1994)]
##print(celebs)
##print(len(celebs))
##
##for (nm, yr) in celebs:
##    if yr < 1980:
##        print(nm)

##students = [("John", ["Comp Sci", "Physics"]),
##    ("Vusi", ["Maths", "Comp Sci", "Stats"]),
##    ("Jess", ["Comp Sci", "Accounting", "Economics", "Management"]),
##    ("Sarah", ["InfSys", "Accounting",   "Economics", "CommLaw"]),
##    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]


# Print all students swith a count of their courses.
##for (name, subjects) in students:
##    print(name + " takes", len(subjects), "courses")
##
##count = 0
##for (name, subjects) in students:
##    for s in subjects:
##        if s == "Comp Sci":
##            count += 1
##print("The number of people taking Comp Sci is ", count)

##def sqrt(n):
##    """Calculate Square root of a number"""
##    approx = n/2.0
##    while True:
##        better = (approx + n/approx)/2.0
##        if abs(approx - better) < 0.001:
##            return better
##        approx = better
##
##
##
##print(sqrt(25.0))
##print(sqrt(49.0))
##print(sqrt(81.0))

##print("Excercise 7")
##print("No 1")
##
##def odd_fn(k):
##    count = 0
##    msg = ""
##    for i in k:
##        if i % 2 != 0:
##            count +=1
##    print( msg + "There are " + str(count) + " Odd Numbers in the set.")
##
##
##odd_fn([5, 6, 7, 2,9, 45, 67, 84])


##print("No 2")
##
##def sum_even(k):
##    sum = 0
##    for i in k:
##        if i % 2 == 0:
##            sum +=i
##        print(sum)
##
##
##sum_even([5, 6, 7, 2,9, 45, 67, 84])

##print("No 3")
##
##def sum_nega(k):
##    sum = 0
##    for i in k:
##        if i < 0:
##            sum +=i
##    print(sum)
##
##sum_nega([5, -6, 7, -2,9, 45, 67, -84])


##print("No 4")
##
##def no_fiv_let_wor(k):
##    count = 0
##    for i in k:
##        if len(i) == 5:
##            count +=1
##    print("There is(are) " + str(count) + " five-letter words in the list")
##
##no_fiv_let_wor(["count", "how", "many", "words", "have", "five", "length"])

##print("No 5")
##
##def sum_to_fir_ev(k):
##    sum = 0
##    for i in k:
##        if i % 2 == 0:
##            break
##        sum = sum + i
##    print(sum)
##
##
##sum_to_fir_ev([1, 3, 5, 7, 9, 2, 11, 8, 10])

##print("No 6")
##
##def sum_to_sam(k):
##    count =  0
##    for i in k:
##        count +=1
##        if i == "sam":
##            break
##    return count

##print("No 7")

##def sqrt(n):
##    """Calculate Square root of a number"""
##    approx = n/2.0
##    while True:
##        better = (approx + n/approx)/2.0
##        if abs(approx - better) < 0.001:
##            break
##        approx = better
##        print(better)
##    print(better)
##
##sqrt(25.0)

##print("No 10")

##def is_prime(k):
##    if k > 2:
##        for i in range(2, k):
##            if k % i == 0:
##                return bool(0)
##        return bool(1)
##    else:
##        print("Please input a number greater than 2")

##print("No 11")
##import turtle
##def mov_drunk_pirate(k):
##    wn = turtle.Screen()
##    wn.bgcolor("hotpink")
##    wn.title("A Drunk Pirate")
##    drunk_man = turtle.Turtle()
##    drunk_man.color("brown")
##    drunk_man.shape("turtle")
##    drunk_man.pensize(3)
##    for (tur, fwd) in k:
##        drunk_man.left(tur)
##        drunk_man.forward(fwd)
##    wn.mainloop()
##
##mov_drunk_pirate([(160, 20), (-43, 10), (270, 8), (-43, 12)])


##print("No 12")
##import turtle

##def drw_pat(k):
##    wn = turtle.Screen()
##    wn.bgcolor("white")
##    wn.title("Euler Graph")
##    a_pat = turtle.Turtle()
##    a_pat.color("black")
##    a_pat.pensize(3)
##    for (trn, dis) in k:
##        a_pat.left(trn)
##        a_pat.forward(dis)
##    wn.mainloop()
##
##drw_pat([(90, 216), (-90, 162), (-126.87, 270), (126.87, 162), (90, 216),
##    (30, 162), (120, 162), (66.87, 270)])


##print("No 14")
##
##def num_digits(n):
##    count = 0
##    if n == 0 or (n < 0 and n > -2):
##        return 1
##    elif n > 0:
##        while n != 0:
##            count = count + 1
##            n = n // 10
##        return count
##    else:
##        while True:
##            count +=1
##            n = n // 10
##            if n < 0 and n > -10:
##                return count + 1

##print(num_digits(-1.9))


##print("No 15")
##
##def num_even_digits(n):
##    count = 0
##    if n > 0:
##        while n != 0:
##            if n % 2 == 0:
##                count +=1
##            n = n // 10
##        return count
##    elif n <= 0 and n > -10:
##        if n % 2 == 0:
##            return 1
##    else:
##        while True:
##            if n % 2 == 0:
##                count +=1
##            n = n // 10
##            if n > -10:
##                if n % 2 == 0:
##                    count +=1
##                return count


##print("No 16")
##
##def sum_of_squares(xs):
##    sum = 0
##    for i in xs:
##        sum += i * i
##    return sum

##print("No 17")
##
### Your friend will complete this function
##def play_once(human_plays_first):
##    """
##       Must play one round of the game. If the parameter
##       is True, the human gets to play first, else the
##       computer gets to play first.  When the round ends,
##       the return value of the function is one of
##       -1 (human wins),  0 (game drawn),   1 (computer wins).
##    """
##    # This is all dummy scaffolding code right at the moment...
##    import random                  # See Modules chapter ...
##    rng = random.Random()
##    # Pick a random result between -1 and 1.
##    result = rng.randrange(-1,2)
##    print("Human plays first={0},  winner={1} "
##                       .format(human_plays_first, result))
##    return result
##
##computer_win = 0
##player_win = 0
##draw = 0
##score = "(You-{}  I-{}   Draw-{})"
##play_again = True
##human_plays_first = True
##while True:
##    if human_plays_first == True:
##        human_plays_first = False
##        a = play_once(human_plays_first)
##        if a  == -1:
##            player_win +=1
##            print("You win!", score.format(player_win, computer_win, draw),
##            "\nYou have won", (player_win * 100 / (player_win + draw + computer_win)), "% of games played!")
##        elif a == 0:
##            draw +=1
##            print("Game drawn!", score.format(player_win, computer_win, draw),
##            "\nYou have won", (player_win * 100 / (player_win + draw + computer_win)), "% of games played!")
##        else:
##            computer_win +=1
##            print("I win!", score.format(player_win, computer_win, draw),
##            "\nYou have won", (player_win * 100 / (player_win + draw + computer_win)), "% of games played!")
##        play_again = input("Do you want to play again? (True / False)")
##        if play_again != "True":
##            break
##    else:
##        human_plays_first = True
##        a = play_once(human_plays_first)
##        if a  == -1:
##            player_win +=1
##            print("You win!", score.format(player_win, computer_win, draw),
##            "\nYou have won", (player_win * 100 / (player_win + draw + computer_win)), "% of games played!")
##        elif a == 0:
##            draw +=1
##            print("Game drawn!", score.format(player_win, computer_win, draw),
##            "\nYou have won", (player_win * 100 / (player_win + draw + computer_win)), "% of games played!")
##        else:
##            computer_win +=1
##            print("I win!", score.format(player_win, computer_win, draw),
##            "\nYou have won", (player_win * 100 / (player_win + draw + computer_win)), "% of games played!")
##        play_again = input("Do you want to play again? (True / False)")
##        if play_again != "True":
##            break
##print("Goodbye")






def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
##    test(mysum([1, 2, 3, 4]) == 10)
##    test(mysum([1.25, 2.5, 1.75]) == 5.5)
##    test(mysum([1, -2, 3]) == 2)
##    test(mysum([ ]) == 0)
##    test(mysum(range(11)) == 55)
##    test(sum_to(4) == 10)
##    test(sum_to(1000) == 500500)
##    test(num_zero_and_five_digits(1055030250) == 7)
##    test(sum_to_sam(["boy", "girl", "sam", "man"]) == 3)
##    test(sum_to_sam(["sam", "boy", "girl", "man"]) == 1)
##    test(sum_to_sam(["boy", "girl", "man", "adam"]) == 4)
##    test(is_prime(11) == True)
##    test(not is_prime(35) == True)
##    test(is_prime(19911121) == True)
##    test(num_even_digits(123456) == 3)
##    test(num_even_digits(2468) == 4)
##    test(num_even_digits(1357) == 0)
##    test(num_even_digits(0) == 1)
##    test(num_even_digits(-23456) == 3)
##    test(sum_of_squares([2, 3, 4]) == 29)
##    test(sum_of_squares([ ]) == 0)
##    test(sum_of_squares([2, -3, 4]) == 29)


##test_suite()        # Here is the call to run the tests








