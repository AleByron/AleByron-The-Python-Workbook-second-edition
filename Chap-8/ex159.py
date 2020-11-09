import random
try:
    inp = open('C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\Words.txt')
    inp = inp.read()
    inp = inp.split()

    for x in inp:
        if len(x)>=3:
            pass
        else:
            inp.remove(x)
    print(inp)
    password = ''
    while password == '':
        elem = random.choices(inp, k=2)
        elem[0] = elem[0].title()
        elem[1] = elem[1].title()
        password = elem[0]+elem[1]
        if len(password)>=8:
            pass
        else:
            password = ''
    print(password)

except ValueError:
    print('Something went wrong, the program will quit')
