n = int(input('Number of units:'))
u = str(input('Unit of measure:'))

if u == 'teaspoons':
    cup = 0
    tab = 0
    teas = n
    if teas >= 3:
        at = teas // 3
        tab = tab + at
        teas = teas % 3

    if tab >= 16:
        tt = tab // 16
        cup = cup + tt
        tab = tab % 16
elif u == 'tablespoons':
    cup = 0
    tab = n
    teas = 0
    if tab >= 16:
        tt = tab // 16
        cup = cup + tt
        tab = tab % 16
elif u == 'cup':
    cup = n
    tab = 0
    teas = 0
else:
    cup = 0
    tab = 0
    teas = 0

print(cup,'Cups', tab,'Tablespoons', teas,'Teaspoons')







