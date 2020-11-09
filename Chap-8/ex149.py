import sys

if len(sys.argv) != 2:
    print("Provide the file name as a command line argument.")
    quit()
try:
    inf = open(sys.argv[1], "r")
    line = inf.readline()
    count = 0
    while count < 10 and line != "":
        line = line.rstrip()
        count = count + 1
        print(line)
        line = inf.readline()
    inf.close()

except IOError:
    print("An error occurred while accessing the file.")

