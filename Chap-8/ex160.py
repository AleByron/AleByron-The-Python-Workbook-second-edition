try:
    inf = open('C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\Cie.txt')
    inf = inf.read()
    inf = inf.split()
    ie_list = []
    fl_rul= []
    not_fl_rul = []
    for i in inf:
        x = 0
        i = i.lower()
        if i not in ie_list:
            while x < len(i)-1:
                if (i[x]=='i' and i[x+1]=='e') or (i[x]=='e' and i[x+1]=='i'):
                    ie_list.append(i)
                x = x+1
    print(ie_list)
    for y in ie_list:
        x=0
        z = 0
        while x < len(y)-1:
            if (y[x]=='i' and y[x+1]=='e'):
                fl_rul.append(y)
            elif (y[x]=='e' and y[x+1]=='i'):
                while z < len(y)-1:
                    if (y[z] == 'c' and y[z + 1] == 'e'):
                        if (y not in not_fl_rul) and (y not in fl_rul):
                            print('a',y)
                            fl_rul.append(y)
                    z = z+1
            x = x+1
    for y in ie_list:
        if y not in fl_rul:
            not_fl_rul.append(y)

    print('List of words that follow the rule:', fl_rul,'\n List of words that don\' follow the rule:', not_fl_rul)


except FileNotFoundError:
    print('Something went wrong, the program is quitting')
    quit()