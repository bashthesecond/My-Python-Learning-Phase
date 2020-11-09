import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
##
##
##
##def remove_vowels(s):
##    vowels = "aeiouAEIOU"
##    no_vowels = ""
##    for i in s:
##        if i not in vowels:
##            no_vowels +=i
##    return no_vowels
##
##
##def find(string, ch):
##    """Return the index of a character in a string, if absent return -1
##    """
##    ind = 0
##    while ind < len(string):
##        if string[ind] == ch:
##            return ind
##        ind +=1
##    return -1
##
##
##def count_a(text):
##    """Counts the number of a in a string
##    """
##    count = 0
##    for k in text:
##        if k == "a":
##            count +=1
##    return count
##
##def find2(strng, ch, start):
##    """Determines position of a character in a string with a search start position
##    """
##    while start < len(strng):
##        if strng[start] == ch:
##            return start
##        start +=1
##    return -1
##
##
##def find3(strng, ch, start=0):
##    """Adding an optional positional referencing introduced in find2
##    """
##    ix = start
##    while ix < len(strng):
##        if strng[ix] == ch:
##            return ix
##        ix +=1
##    return -1
##
##
##def find(strng, ch, start=0, end=None):
##    """Added an optional end positioning to the begining used in find3 above.
##    """
##    ix = start
##    if end == None:
##        end = len(strng)
##    while ix < end:
##        if strng[ix] == ch:
##            return ix
##        ix +=1
##    return -1
##
##punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
##def remove_punctuation(s):
##    """removes punctuation from a string of words
##    """
##    s_sans_punct = ""
##    for k in s:
##        if k not in punctuation:
##            s_sans_punct +=k
##    return s_sans_punct
##
##
##import string
##def remove_punctuation(s):
##    """Using the inbuilt python method of removing punctuations
##    """
##    s_without_punct = ""
##    for letter in s:
##        if letter not in string.punctuation:
##            s_without_punct +=letter
##    return s_without_punct
##
##
##my_story = """
##Pythons are constrictors, which means that they will 'squeeze' the life
##out of their prey. They coil themselves around their prey and with
##each breath the creature takes the snake will squeeze a little tighter
##until they stop breathing completely. Once the heart stops the prey
##is swallowed whole. The entire animal is digested in the snake's
##stomach except for fur or feathers. What do you think happens to the fur,
##feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
##you guessed it --- snake POOP! """
##
##wds = remove_punctuation(my_story).split()
##print(wds)
##
##
##n1 = "Paris"
##n2 = "Whitney"
##n3 = "Hilton"
##
##print("Pi to three decimal places is {0:.3f}".format(3.1415926))
##print("123456789 123456789 123456789 123456789 123456789 123456789")
##print("|||{0:<15}|||{1:^15}|||{2:>15}|||Born in {3}|||".format(n1,n2,n3,1981))
##print("The decimal value {0} converts to hex value {0:x}".format(123456))
##
##
##letter = """
##Dear {0} {2}.
##    {0}, I have an interesting money-making proposition for you! If you deposit
##$10million into my bank account, I can double your money...
##"""
##print(letter.format("Paris", "Whitney", "Hilton"))
##print(letter.format("Bill", "Henry", "Gates"))


##print("i\ti**2\ti**3\ti**5\ti**10\ti**20")
##for i in range(1, 11):
##    print(i, "\t", i**2, "\t", i**3, "\t", i**5, "\t",
##                                            i**10, "\t", i**20)


##layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"
##print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
##for i in range(1, 11):
##    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))


##print("Exercise 1")
##print("No 2")
##
##prefixes = "JKLMNOPQ"
##suffix = "ack"
##
##for letter in prefixes:
##    if letter == "O" or letter == "Q":
##        print(letter + "u" + suffix)
##    else:
##        print(letter + suffix)


##print("No 3")
##
##def count_letters(strng, ch):
##    count = 0
##    for letter in strng:
##        if letter == ch:
##            count +=1
##    return count

##
##print("No 4")
##
##def find(strng, ch, start=0):
##    count = 0
##    count_1 = 0
##    c = ""
##    if start != 0:
##        while True:
##            a = strng[count:].find(ch)
##            if a!= -1:
##                count_1 +=1
##                b = count + a + 1
##                print(b, end="   ")
##                count = b
##            else:
##                print("")
##                print("search completed, ", count_1, " indexes found")
##                break
##    else:
##        a= strng.find(ch)
##        if a == -1:
##            print("search completed, 0 indexes found")
##        else:
##            print("index found: ", a)
##
##
##find("barman", "a", 1)



##print("No 5")
##
##import string
##def sort_sent(s):
##    sen_without_punc = ""
##    count = 0
##    count_words = 0
##    for word in s:
##        if word != string.punctuation:
##            sen_without_punc +=word
##    a =sen_without_punc.split()
##    for word in a:
##        count_words +=1
##    for word in a:
##        if "e" in word:
##            count +=1
##    no_e_in_per = count * 100/ count_words
##    print("your text contain ", count_words, " word(s), of which ", count,
##    "({0:.2f}%) contains an 'e'.".format(no_e_in_per))
##
##
##var_cal ="""The whole subject of calculus is built on the relation between u and f. The question
##we are raising here is not some kind of joke, after which the book will get serious
##and the mathematics will get started.
##"""
##sort_sent(var_cal)


##print("No 6")
##
##def mul_tab():
##    """Prints a well formatted 12-times table
##    """
##    layout = "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>5}{10:>5}{11:>5}"
##    for i in range(1, 13):
##        print(layout.format(i*1, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10,\
##        i*11, i*12))
##
##mul_tab()

##print("No 7")
##
##def reverse(x):
##    emp_word = ""
##    for i in range(1, len(x) + 1):
##        emp_word += x[-i]
##    return(emp_word)


##print("No 8")
##
##def mirror(x):
##    emp_word = "" + x
##    for i in range(1, len(x) + 1):
##        emp_word += x[-i]
##    return(emp_word)


##print("No 9")
##
##def remove_letter(ch, strng):
##    emp_wrd = ""
##    for i in strng:
##        if i != ch:
##            emp_wrd +=i
##    return emp_wrd
##

##print("No 10")
##
##def is_palindrome(x):
##    emp_word = ""
##    for i in range(1, len(x) + 1):
##        emp_word += x[-i]
##    if emp_word == x:
##        return True
##    else:
##        return False


##print("No 11")
##
##def count(ch, strng):
##    count = 0
##    find_ch = -1
##    while True:
##        find_ch = strng.find(ch, find_ch + 1)
##        if find_ch != -1:
##            count +=1
##        else:
##            break
##    return count


##print("No 12")
##def remove(ch, strng):
##    nw_wrd =""
##    ind_po = strng.find(ch)
##    count = 0
##    if ind_po != -1:
##        for i in strng:
##            count +=1
##            if count <= ind_po:
##                nw_wrd +=i
##            elif count > ind_po and count <= ind_po + len(ch):
##                continue
##            else:
##                nw_wrd +=i
##        return nw_wrd
##    else:
##        return strng


##print("No 13")
##
##def remove_all(ch, strng):
##    """To remove all occurence of a substring, "ch" in a string, "strng".
##    """
##    emp_word = ""
##    start = 0
##    while start < len(strng):
##        if strng[start:start + len(ch)] == ch:
##            start = start + len(ch)
##        else:
##            emp_word += strng[start]
##            start +=1
##    return emp_word




def test_suite():
##    """ Run the suite of tests for code in this module (this file).
##    """
##    test(remove_vowels("compsci") == "cmpsc")
##    test(remove_vowels("aAbEefIijOopUus") == "bfjps")
##    test(find("Compsci", "p") == 3)
##    test(find("Compsci", "C") == 0)
##    test(find("Compsci", "i") == 6)
##    test(find("Compsci", "x") == -1)
##    test(count_a("banana") == 3)
##    test(find2("banana", "a", 2) == 3)
##    ss = "Python strings have some interesting methods."
##    test(find(ss, "s") == 7)
##    test(find(ss, "s", 7) == 7)
##    test(find(ss, "s", 8) == 13)
##    test(find(ss, "s", 8, 13) == -1)
##    test(find(ss, ".") == len(ss)-1)
##    test(remove_punctuation('"Well, I never did!", said Alice.') ==
##                                "Well I never did said Alice")
##    test(remove_punctuation("Are you very, very, sure?") ==
##                                 "Are you very very sure")
##    test(reverse("happy") == "yppah")
##    test(reverse("Python") == "nohtyP")
##    test(reverse("") == "")
##    test(reverse("a") == "a")
##    test(mirror("good") == "gooddoog")
##    test(mirror("Python") == "PythonnohtyP")
##    test(mirror("") == "")
##    test(mirror("a") == "aa")
##    test(remove_letter("a", "apple") == "pple")
##    test(remove_letter("a", "banana") == "bnn")
##    test(remove_letter("z", "banana") == "banana")
##    test(remove_letter("i", "Mississippi") == "Msssspp")
##    test(remove_letter("b", "") == "")
##    test(remove_letter("b", "c") == "c")
##    test(is_palindrome("abba"))
##    test(not is_palindrome("abab"))
##    test(is_palindrome("tenet"))
##    test(not is_palindrome("banana"))
##    test(is_palindrome("straw warts"))
##    test(is_palindrome("a"))
##    test(count("is", "Mississippi") == 2)
##    test(count("an", "banana") == 2)
##    test(count("ana", "banana") == 2)
##    test(count("nana", "banana") == 1)
##    test(count("nanan", "banana") == 0)
##    test(count("aaa", "aaaaaa") == 4)
##    test(remove("an", "banana") == "bana")
##    test(remove("cyc", "bicycle") == "bile")
##    test(remove("iss", "Mississippi") == "Missippi")
##    test(remove("eggs", "bicycle") == "bicycle")
##    test(remove_all("an", "banana") == "ba")
##    test(remove_all("cyc", "bicycle") == "bile")
##    test(remove_all("iss", "Mississippi") == "Mippi")
##    test(remove_all("eggs", "bicycle") == "bicycle")




test_suite()    # Here is the call to run the tests

