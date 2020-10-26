from ex117 import splitWords

def listof(list):
    list = list
    string = ''

    a = 0

    for i in list:
        y = splitWords(i)
        while a <= len(y):
            if a < len(y) - 2:
                string = string + y[a] + ',' + ' '
            elif a == len(y) - 2:
                string = string + y[a] + ' ' + 'and' + ' '
            elif a == len(y) - 1:
                string = string + y[a] + '.' + '\n'
            a = a + 1
        a = 0


    return string

def main():
    lista = []
    while 0 < 1:
        x = str(input('Enter an element of your list:'))
        if x == '':
            break
        lista.append(x)

    print(listof(lista))

main()









