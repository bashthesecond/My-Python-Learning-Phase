myfile = open("test2.txt", "w")
myfile.write("My second file written from Python\n")
myfile.write("----------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()
myfile = open("test3.txt", "w")
myfile.write("Using same handler to write in a new file\n")
myfile.write("It is actually possible to achieve it if done in a sequence\n")
myfile.write("PASSED!\n")
myfile.close()
mynewhandle = open("test2.txt", "r")
while True:                                 #keep reading
    theline = mynewhandle.readline()        #try to read line
    if len(theline) == 0:
        break
    #process read line next
    print(theline, end ="")

mynewhandle.close()


f = open("test3.txt", "r")
xs = f.readlines()
f.close()

xs.sort()
g = open("sortedtest3.txt", "w")
for v in xs:
    g.write(v)
g.close()

