def spell(a):
    dict = {'a':'Alpha', 'b':'Bravo', 'c':'Charlie', 'd':'Delta', 'e':'Echo', 'f':'Foxtrot', 'g':'Golf', 'h':'Hotel', 'i':'India', 'j':'Juliet', 'k':'Kilo', 'l':'Lima', 'm':'Mike', 'n':'November','o':'Oscar', 'p':'Papa', 'q':'Quebec', 'r':'Romeo', 's':'Sierra', 't':'Tango', 'u':'Uniform', 'v':'Victor', 'w':'Whiskey', 'x':'Xray', 'y':'Yankee', 'z':'Zulu'}
    if len(a) == 0:
        return a
    else:
        if a[0] in dict:
            res = dict[a[0]] + ' ' + spell(a[1:])
            return res

def main():
    a = str(input('Enter a message: '))
    print(spell(a))

main()