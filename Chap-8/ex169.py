

inf = input('Enter the file name you want to use to redact your text file:')
inf2 = input('Enter the text file to redact:')

try:
    red = open('C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\' + inf, 'r')
    redstr = red.read()
    redlist = redstr.split()
    print(redlist)



except FileNotFoundError:
    print('Something went wrong with your redact file, the program wil quit')
    quit()

try:
    tored = open('C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\' + inf2, 'r')
    toredarr = tored.read()
    toredarrtest = toredarr.lower()
    #toredarr = toredarr.split()
    for check in redlist:
        if check in toredarrtest:
            toredarrtest = toredarrtest.replace(check, '*'*len(check))
    print(toredarrtest)

    x = 0
    final = ''
    for letter in toredarr:
        print(letter)
        if letter != toredarrtest[x] and toredarrtest[x]=='*':
            letter = '*'
            final = final + letter
        else:
            letter = letter
            final = final + letter
        x = x+1
    print(final)

    fin = open('C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\' + 'RedactedDocument.txt', 'a')
    fin.write(final)
    fin.close()

except FileNotFoundError:
    print('Something went wrong with your text file, the program wil quit')
    quit()


