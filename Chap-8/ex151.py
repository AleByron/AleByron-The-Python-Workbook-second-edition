import sys

if len(sys.argv) < 2:
    print("Provide other file names as command line arguments.")
    quit()
try:
    for i in range(len(sys.argv)):
        if i >0:
            inf = open(sys.argv[i], "r")
            line = inf.readlines()
            print(line)
            inf.close()

except IOError:
    print("An error occurred while accessing the file.")