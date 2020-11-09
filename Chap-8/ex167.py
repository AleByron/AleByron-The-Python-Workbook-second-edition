from ex117 import splitWords
import sys

inp = input('Enter the words you want to check:')

if len(sys.argv) != 2:
    print("Error in searching your checker file, no argument provided, the program will quit.")
    quit()

try:
    inf = open(sys.argv[1], 'r')
    check = inf.read()
    check = check.lower()
    words = splitWords(inp)
    errors = []
    for w in words:
        if w in check:
            pass
        else:
            errors.append(w)

    print(errors)

except FileNotFoundError:
    print('Something went wrong with your check file, the program wil quit')
    quit()

