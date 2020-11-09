from ex117 import splitWords
fname = input("Enter the file name: ")
fname = 'C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\' + fname
dec = {}

try:
    inf = open(fname, "r")
    line = inf.readline()
    text = line.split()
    c = 0
    while c <= len(line) + 1 and line != "":
        line = inf.readline()
        text = line.split()
        for i in text:
            i = i.lower()
            if i not in dec:
                dec[i] = 1
            else:
                dec[i] = dec[i]+1

        c = c+1
    print(dec)
except FileNotFoundError:
    print("File could not be opened. Quitting...")
    quit()