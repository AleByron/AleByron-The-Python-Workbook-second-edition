import sys

if len(sys.argv) < 2:
    print("Error in searching your checker file, no argument provided, the program will quit.")
    quit()

try:
    inf = open(sys.argv[1], 'r')
    file = inf.read()
    file = file.split()
    x = 1
    while file!=[]:
        line = ''
        while len(line)<=50 and file !=[]:
            if len(line + file[0] + ' ')<=50:
                line = line + file[0] + ' '
            else:
                break
            file.pop(0)
        print(line)

except FileNotFoundError:
    print('Something went wrong with your check file, the program wil quit')
    quit()