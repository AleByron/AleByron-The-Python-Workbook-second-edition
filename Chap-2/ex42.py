note = str(input('Insert a note:'))
ch = note[0]
n = note[1]
n = int(n)
if ch == 'C':
    f = 261.63
    f = f/(2**(4-n))
elif ch == 'D':
    f = 293.66
    f = f / (2 ** (4 - n))
elif ch == 'E':
    f = 329.63
    f = f / (2 ** (4 - n))
elif ch == 'F':
    f = 349.23
    f = f / (2 ** (4 - n))
elif ch == 'G':
    f = 392.00
    f = f / (2 ** (4 - n))
elif ch == 'A':
    f = 440.00
    f = f / (2 ** (4 - n))
elif ch == 'B':
    f = 493.88
    f = f / (2 ** (4 - n))
else:
    print('This is not a note')
print(f)
