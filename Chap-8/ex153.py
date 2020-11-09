try:
    inf = open('C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\TestFile.txt', "r")
    text = inf.read()
    spl = text.split()
    print(spl)
    L_Word = 0
    N_Word = 0
    for i in spl:
        if len(i) > L_Word:
            L_Word = len(i)
            The_Word = i
        elif len(i) == L_Word:
            N_Word = N_Word +1
        elif len(i)<L_Word:
            pass
    print('The longer word is', The_Word,'with', L_Word,' characters. \n There are also other', N_Word,'with this length.')

except FileNotFoundError:
    print("File could not be opened. Quitting...")
    quit()