import sys
import os

if len(sys.argv) < 2:
    print("Error in searching your checker file, no argument provided, the program will quit.")
    quit()
try:
    x = 0

    res ={}
    while x<len(sys.argv)-1:
        l_counter = 0
        inf = open(sys.argv[x+1], 'r')
        res.setdefault('File: ' + str(os.path.basename(sys.argv[x+1])), [])

        lines = inf.readlines()
        for l in lines:
            l_counter = l_counter +1
            if l[0:3]=='def' and lines[l_counter-1][0] != '#':
                res['File: ' + str(os.path.basename(sys.argv[x+1]))].append('Line number: '+str(l_counter) + ' Function name: ' + l[0:len(l)-2])

        x = x+1
    print(res)


except FileNotFoundError:
    print('Something went wrong with your check file, the program wil quit')
    quit()
