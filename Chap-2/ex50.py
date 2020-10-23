m = float(input('Insert a magnitude:'))
if m < 2:
    mess='micro'
elif 2 < m < 3:
    mess = 'very minor'
elif 3 < m < 4:
    mess = 'minor'
elif 4 < m < 5:
    mess = 'light'
elif 5 < m < 6:
    mess = 'moderate'
elif 6 < m < 7:
    mess = 'strong'
elif 7 < m < 8:
    mess = 'major'
elif 8 < m < 10:
    mess = 'great'
elif m > 10:
    mess = 'meteoric'

print('This earthquake is', mess)
