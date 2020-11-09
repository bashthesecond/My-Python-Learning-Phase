##myfile = open("test.txt", "w")
##myfile.write("My first file written from Python\n")
##myfile.write("---------------------------------\n")
##myfile.write("Hello, world!\n")
##myfile.close()


##
##mynewhandle = open("test.txt", "r")
##while True:
##    theline = mynewhandle.readline()
##    if len(theline) == 0:
##        break
##    print(theline, end="")
##mynewhandle.close()

##f = open("test.txt")
##xs = f.read()
##f.close()
##
##words = xs.split()
##print("There are {0} words in the file".format(len(words)))


##f = open("NO.jpg", "rb")
##g = open("new_NO.jpg", "wb")
##
##while True:
##    buf = f.read(1024)
##    if len(buf) == 0:
##        break
##    g.write(buf)
##
##f.close()
##g.close()

#import urllib.request
##url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Simple_Soccer_Ball.svg/200px-Simple_Soccer_Ball.svg.png"
##destination_filename = "ball.jpg"
##urllib.request.urlretrieve(url, destination_filename)

##print("exercise 1")
##def reverse_file(old_file, new_file):
##    in_file = open(old_file, "r")
##    out_file = open(new_file, "w")
##    xs = in_file.readlines()
##    xs.reverse()
##    for i in xs:
##        out_file.write(i)
##    in_file.close()
##    out_file.close()


##print("exercise 2")
##def file_with_snake(fle):
##    in_file = open(fle, "r")
##    xs = in_file.readlines()
##    for i in xs:
##        if "snake" in i:
##            print(i, end= "")


##def number_file(old_file):
##    infile = open(old_file, "r")
##    outfile = open("output_file.txt", "w")
##    count = 1
##    while True:
##        xs = infile.readline()
##        if len(xs) == 0:
##            break
##        a = "{:>4} ".format(count) + xs
##        outfile.write(a)
##        print(a, end="")
##        count +=1
##    infile.close()
##    outfile.close()
##
##number_file("number_file_test.txt")





##def remove_number_in_file(xs):
##    infile = open(xs)
##    outfile = open("output_file_2.txt", "w")
##    xs = infile.readlines()
##    for i in xs:
##        outfile.write(i[5:])
##    infile.close()
##    outfile.close()
##
##remove_number_in_file("remove_number_file_test.txt")


