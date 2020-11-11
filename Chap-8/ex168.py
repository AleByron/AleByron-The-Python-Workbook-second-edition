import sys

if len(sys.argv) != 2:
    print("Error in searching your checker file, no argument provided, the program will quit.")
    quit()

errors = {}
finals = ['']
try:
    inf = open(sys.argv[1], 'r')
    inf = inf.readlines()
    counter2 = 1
    for line in inf:
        line = line.lower()
        spl = line.split()
        counter = 0
        print(counter2)
        finals.append(spl[len(spl)-1])
        if finals[counter2-1] == spl[0]:
            errors.setdefault('Line' + str(counter2), [])
            errors['Line' + str(counter2)].append(spl[counter])
        while counter < len(spl)-1:
            if spl[counter] == spl[counter+1]:
                errors.setdefault('Line' + str(counter2), [])
                errors['Line'+str(counter2)].append(spl[counter])
            counter = counter +1
        counter2 = counter2 +1

    print(errors)

except FileNotFoundError:
    print('Something went wrong with your check file, the program wil quit')
    quit()