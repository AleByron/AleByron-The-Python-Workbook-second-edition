x = str(input('Insert a grade:'))
tot = [x]
totn = [] #array of grades in float
sum = 0 #This is the sum fo grades
while x != '':
    x = str(input('Insert another grade:'))
    if x != '':
        tot.append(x)
for x in tot:
    if x == 'A+':
        g = 4.0
        totn.append(g)
    elif x == 'A':
        g = 4.0
        totn.append(g)
    elif x == 'A-':
        g = 3.7
        totn.append(g)
    elif x == 'B+':
        g = 3.3
        totn.append(g)
    elif x == 'B':
        g = 3.0
        totn.append(g)
    elif x == 'B-':
        g = 2.7
        totn.append(g)
    elif x == 'C+':
        g = 2.3
        totn.append(g)
    elif x == 'C':
        g = 2.0
        totn.append(g)
    elif x == 'C-':
        g = 1.7
        totn.append(g)
    elif x == 'D+':
        g = 1.3
        totn.append(g)
    elif x == 'D':
        g = 1.0
        totn.append(g)
    elif x == 'F':
        g = 0
        totn.append(g)
    else:
        g = 'incorrect'

for x in totn:
    sum = sum+x

av = sum/len(totn)
print('The grade averege is',av)