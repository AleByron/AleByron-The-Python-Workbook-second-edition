import math
Ta = float(input('Insert the temperature in degrees:'))
V = float(input('Insert the velocity of the wind in KM/H:'))
WCI = math.floor(13.12 + 0.6215*Ta - 11.37*(V**0.16)+0.3965*Ta*(V**0.16))
print('The WCI is:', WCI)