from unit_tester import test
import time
def search_linear(xs, target):
    for (ind, val) in enumerate(xs):
        if val == target:
            return ind
    return -1


friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
vocab = ["apple", "boy", "dog", "down",
                          "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()


test(search_linear(friends, "Zoe") == 1)
test(search_linear(friends, "Joe") == 0)
test(search_linear(friends, "Paris") == 6)
test(search_linear(friends, "Bill") == -1)


def search_binary(xs, target):
    """searches efficiently through a list returning index"""
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:    #If region of interest(ROI) becomes emoty
            return -1

        #Next probe goes to middle of ROI
        mid_index = (lb + ub) // 2
        #fetch value of item in middle
        item_at_mid = xs[mid_index]
        #print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'
        #    .format(ub, lb, lb-ub, item_at_mid, target))
        #compare probed item with target
        if item_at_mid == target:
            return mid_index    #tada! found it
        if item_at_mid < target:
            lb = mid_index + 1  #redefine the ROI by removing certainty
        else:
            ub = mid_index  ##redefine the ROI by removing certainty

##xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
##test(search_binary(xs, 20) == -1)
##test(search_binary(xs, 99) == -1)
##test(search_binary(xs, 1) == -1)
##for (i, v) in enumerate(xs):
##    test(search_binary(xs, v) == i)



def find_unknown_words(vocab, wds):
    emp =[]
    for w in wds:
        if search_binary(vocab, w) == -1:
            emp.append(w)
    return emp

test(find_unknown_words(vocab, book_words) == ["from", "to"])
test(find_unknown_words([], book_words) == book_words)
test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])



def load_words_from_file(filename):
    """read words from filename and return list of words"""
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds


bigger_vocab = load_words_from_file("vocab.txt")
print("There are {0} words in the vocab, starting with \n {1}"
        .format(len(bigger_vocab), bigger_vocab[:6]))


def text_to_words(the_text):
    """cleans up a string of words, removing punctuations and white spaces
        and returns a list of wprds in lower cases"""
    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
test(text_to_words('"Well, I never!", said Alice.') ==
                             ["well", "i", "never", "said", "alice"])


def get_words_in_book(filename):
    """Read words in book into a list of words"""
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

def remove_adjacent_dups(xs):
    """Return a new list in which all adjacent duplicate from xs have
            been removed"""
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e
    return result

test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
test(remove_adjacent_dups([]) == [])
test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
                                   ["a", "big", "bite", "dog"])


all_words = get_words_in_book("alice_in_wonderland.txt")
all_words.sort()
book_words = remove_adjacent_dups(all_words)
print("There are {0} words in the book, the first 100 are\n{1}".
           format(len(book_words), book_words[:100]))

t0 = time.time()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.time()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))


def merge(xs, ys):
    """meerge two sorted lists to return a single sorted list"""
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result
        if yi >= len(ys):
            result.extend(xs[xi:])
            return result
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]
zs = xs+ys
zs.sort()
test(merge(xs, []) == xs)
test(merge([], ys) == ys)
test(merge([], []) == [])
test(merge(xs, ys) == zs)
test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==
               ["a", "big", "big", "bite", "cat", "dog"])


def find_unknowns_merge_pattern(vocab, wds):
    """ Both the vocab and wds must be sorted.  Return a new
        list of words from wds that do not occur in vocab.
    """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result
        if yi >= len(wds):
            return result
        if vocab[xi] == wds[yi]:
            yi += 1
        elif vocab[xi] < wds[yi]:
            xi += 1
        else:
            result.append(wds[yi])
            yi += 1


##all_words = get_words_in_book("alice_in_wonderland.txt")
##t0 = time.time()
##all_words.sort()
##book_words = remove_adjacent_dups(all_words)
##missing_words = find_unknowns_merge_pattern(bigger_vocab, book_words)
##t1 = time.time()
##print("There are {} unknown words".format(len(missing_words)))
##print("That took {:4f} seconds".format(t1-t0))

def find_commmon_elem_merge_pat(xs, ys):
    """meerge two sorted lists to return a single sorted list"""
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            return result
        if yi >= len(ys):
            return result
        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1

def find_unknowns_merge_pattern_2(xs, ys):
    """merge two sorted lists to return a single sorted list"""
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            return result
        if yi >= len(ys):
            result.extend(xs[xi:])
            return result
        if xs[xi] > ys[yi]:
            yi += 1
        elif xs[xi] == ys[yi]:
            xi += 1
        else:
            result.append(xs[xi])
            xi += 1

def add_all_elem_merge(xs, ys):
    """Return items that are present in either the first or the second list"""
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result
        if yi >= len(ys):
            result.extend(xs[xi:])
            return result
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def bagdiff(xs, ys):
    """Return items from the first list that are not eliminated by a
                matching element in the second list."""
    xi = 0
    yi = 0
    result = []
    if xi >= len(xs):
        return result
    if yi >= len(ys):
        result.extend(xs[xi:])
    if xs[xi] == ys[yi]:
        xi += 1
    elif xs[xi] > ys[yi]:
        yi += 1
    else:
        result.append(xs[xi])
        xi += 1


def share_diagonal(x0, y0, x1, y1):
    """Checks if (x0, x1) and (y0, y1) share same diagonals"""
    dy = abs(y1 - y0)   #calculates absolute distance on y-axis
    dx = abs(x1 - x0)   #calculates absolute distance on x-axis
    return dy == dx     #checks if they share diagonals

test(not share_diagonal(5,2,2,0))
test(share_diagonal(5,2,3,0))
test(share_diagonal(5,2,4,3))
test(share_diagonal(5,2,4,1))


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

# Solutions cases that should not have any clashes
test(not col_clashes([6,4,2,0,5], 4))
test(not col_clashes([6,4,2,0,5,7,1,3], 7))

# More test cases that should mostly clash
test(col_clashes([0,1], 1))
test(col_clashes([5,6], 1))
test(col_clashes([6,5], 1))
test(col_clashes([0,6,4,3], 3))
test(col_clashes([5,0,7], 2))
test(not col_clashes([2,0,1,3], 1))
test(col_clashes([2,0,1,3], 2))



def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

test(not has_clashes([6,4,2,0,5,7,1,3])) # Solution from above
test(has_clashes([4,6,2,0,5,7,1,3]))     # Swap rows of first two
test(has_clashes([0,1,2,3]))             # Try small 4x4 board
test(not has_clashes([2,0,3,1]))         # Solution to 4x4 case

def main():
    import random
    rng = random.Random()   # Instantiate a generator

    bd = list(range(8))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           print("Found solution {0} in {1} tries.".format(bd, tries))
           tries = 0
           num_found += 1

main()
