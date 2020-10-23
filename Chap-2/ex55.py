w = float(input('Insert a wavelength:'))
if 380 <= w <=450:
    c = 'violet'
elif 450 <= w <=495:
    c = 'blue'
elif 495 <= w <=570:
    c = 'green'
elif 570 <= w <= 590:
    c = 'yellow'
elif 590 <= w <= 620:
    c = 'orange'
elif 620 <= w <= 750:
    c = 'red'
else:
    c='This wavelength is not visible '

print(c)