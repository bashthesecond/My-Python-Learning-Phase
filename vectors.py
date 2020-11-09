import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def add_vectors(u, v):
    """adds two vectors (represented as lists) and return a single list
    """
    empty_list = []
    for i in range(len(u)):
        a = u[i] + v[i]
        empty_list.append(a)
    return empty_list

def scalar_mult(s, v):
    """multiplies a scalar value by a vector and gives a result
    """
    empty_list = []
    for i in range(len(v)):
        nw_val = s * v[i]
        empty_list.append(nw_val)
    return empty_list

def dot_product(u, v):
    """multiplies two vectors of equal length to produce a single vector(list)
    element
    """
    nw_value = 0
    for i in range(len(u)):
        temp_val = u[i] * v[i]
        nw_value +=temp_val
    return nw_value


def replace(s, old, new):
    """replaces existence of a previous character in a string with another character
    """
    old_lt = s.split()
    strt = 0
    for i in range(len(old_lt)):
        if old in old_lt[i]:
            new_ch = ""
            while strt < len(old_lt[i]):
                if old_lt[i][strt : strt + len(old)] == old:
                    new_ch += new
                    strt = strt + len(old)
                else:
                    new_ch += old_lt[i][strt]
                    strt += 1
            strt = 0
            old_lt[i] = new_ch
        else:
            continue
    nw_lt = " ".join(old_lt)
    return nw_lt







def test_suite():
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    test(dot_product([1, 1], [1, 1]) ==  2)
    test(dot_product([1, 2], [1, 4]) ==  9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") ==
        "I love spam! Spam is my favorite food. Spam, spam, yum!")
    test(replace(s, "o", "a") ==
        "I lave spam! Spam is my favarite faad. Spam, spam, yum!")


test_suite()    # Here is the call to run the tests