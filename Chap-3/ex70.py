bits = str(input('Enter 8 bits:'))
while bits != '':
    if len(bits) != 8:
        print('This is not a correct bit line')
        bits = ''
    elif len(bits) == 8:
        x = bits.count('1') #number of one in the line
        if x%2 == 0:
           print('The parity bit is 0')
           bits = ''
        else:
            print('The parity bit is 1')
            bits = ''
    else:
        print('This is not a correct bit line')
        bits = ''