s = str(input('Enter an word:'))
sa = []
sa.append(s)
while 0<1:
    s = str(input('Enter another word:'))
    if s == '':
        break
    elif s in sa:
        s=s
    else:
        sa.append(s)




for i in sa:
    print(i)
