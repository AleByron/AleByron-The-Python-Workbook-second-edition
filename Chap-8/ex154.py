fname = input("Enter the file name: ")
fname = 'C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\' + fname
alf = ['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m']
dec = {'q':0,'w':0,'e':0,'r':0,'t':0,'y':0,'u':0,'i':0,'o':0,'p':0,'l':0,'k':0,'j':0,'h':0,'g':0,'f':0,'d':0,'s':0,'a':0,'z':0,'x':0,'c':0,'v':0,'b':0,'n':0,'m':0}

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
            for x in i:
                if x in dec:
                    dec[x] = dec[x]+1
        c = c+1
    print(dec)
except FileNotFoundError:
    print("File could not be opened. Quitting...")
    quit()