fname = input("Enter the file name: ")
fname2 = input('Enter a name for the new file:')
fname = 'C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\' + fname
fname2 = 'C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\' + fname2
# Attempt to open the file
try:
    inf = open(fname, "r")
    line = inf.readline()
    count = 0
    TFile_res = open(fname2, 'a')
    while count <= len(line)+1 and line != "":
        count = count + 1
        line = line.rstrip()
        line = str(count) + ': ' + line + ' ' + '\n'
        TFile_res.write(line)
        line = inf.readline()
    inf.close()

except FileNotFoundError:
    print("File could not be opened. Quitting...")
    quit()

