def splitWords(x):
    p = 5
    list = []
  #  word = ''
    d = 0  # counter for ' <--- exception and general counter
    d1 = 0  # general counter to know where to split the string
  #  d2 = 0  #additional counter
    for a in x:
        if 'a' < a < 'z' or 'A' < a < 'Z' :
            p = 0

        elif a == ' ' or a == ',' or a == '?' or a == '-' or a == '_' or a == '\'' or a == '!' or a == '.' or a == ':':
            p = 1
            d1 = d - d1
            #to handle the ' <---exception
            if a == '\'':
                c = d + 1
                b = x[d:c]
                if b != ' ':
                    p = 0
        # focus the word to split
        if p == 1:
            word = x[d1:d]
            d2 = len(word)
            list.append(word)
            d1 = d - d2 - d1 - 1
            p = 0

        d = d + 1
        d1 = d1 + 1
        #to take the last word
        if len(x) == d:
            d1 = d - d1
            word = x[d1:d]
            list.append(word)

            p = 0

    for i in list:
        if i == '':
            list.remove(i)

    return list


def main():
    string = str(input('Insert a string:'))
    print(splitWords(string))

if __name__ == "__main__":
    main()