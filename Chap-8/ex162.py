from ex117 import splitWords
alph = {}
perc = {}
try:
    inf = open('C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\String.txt')
    inf = inf.read()
    words = splitWords(inf)
    print(words)
    tot = 0
    for w in words:
        for l in w:
            l = l.lower()
            if l not in alph and 'a'<=l<='z':
                alph[l] = 1
                tot = tot+1
            elif 'a'<=l<='z':
                alph[l] = alph[l] +1
                tot = tot+1

    for l in alph:
        a = round(alph[l]*100/tot,2)
        perc[l] = str(a) + '%'

    print(perc)

except FileNotFoundError:
    print('Something went wrong, the program wil quit')
    quit()