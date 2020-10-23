x = str(input('Insert a grade:'))
if x == 'A+':
    g = 4.0
elif x == 'A':
    g = 4.0
elif x == 'A-':
    g = 3.7
elif x == 'B+':
    g = 3.3
elif x == 'B':
    g = 3.0
elif x == 'B-':
    g = 2.7
elif x == 'C+':
    g = 2.3
elif x == 'C':
    g = 2.0
elif x == 'C-':
    g = 1.7
elif x == 'D+':
    g = 1.3
elif x == 'D':
    g = 1.0
elif x == 'F':
    g = 0
else:
    g = 'incorrect'

print('the grade you inserted is', g)