pos = str(input('Insert a position on the chess board:'))
pos = pos.lower()
l = pos[0]
n = int(pos[1])
n2 = n%2
if l == 'a' or l == 'c' or l == 'e' or l == 'g':
    if n2 == 0 and n>=2:
        c = 'white'
    else:
        c = 'black'
else:
    if n2 == 0 and n>=2:
        c = 'black'
    else:
        c = 'white'

print(c)