import sys

if len(sys.argv) != 2:
    print("Provide the file name as a command line argument.")
    quit()
try:
    inf = open(sys.argv[1], "r")
    line = inf.readlines()
    a = len(line)
    b = len(line)-10
    if b >= 1:
        z = 0
        while z < b:
            line.pop(0)
            z = z+1
    print(line)
    inf.close()

except IOError:
    print("An error occurred while accessing the file.")