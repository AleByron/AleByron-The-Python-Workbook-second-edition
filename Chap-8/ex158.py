try:
    inp = open('C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\prova.py', 'r')
    lines = inp.readlines()
    print(lines)
    for line in lines:
        print(line)
        if line[0] == '#':
            pass
        else:
            try:
                out = open('C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\TestFileWrite.txt', 'a')
                out.write(line)


            except FileNotFoundError:
                print('Something with your output file went wrong, the program will quit.')
                quit()


except FileNotFoundError:
    print('Something with your input file went wrong, the program will quit.')
    quit()

