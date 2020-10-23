f = float(input('Insert a radiation frequency:'))
if  3*(10**9) < f:
    w = 'radio waves'
elif 3*(10**9) <= f < 3*(10**12):
    w = 'microwaves'
elif 3 * (10 ** 12) <= f < 4.3 * (10 ** 14):
    w = 'infrared light'
elif 4.3 * (10 ** 14) <= f < 7.5 * (10 ** 14):
    w = 'visible light'
elif 7.5 * (10 ** 14) <= f < 3 * (10 ** 17):
    w = 'ultraviolet light'
elif 3 * (10 ** 17) <= f < 3 * (10 ** 19):
    w = 'X-Rays'
elif f > 3 * (10 ** 19):
    w = 'Gamma Rays'

print('It is', w)