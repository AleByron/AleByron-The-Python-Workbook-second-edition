f, i = input("Insert your height in feets and inches:").split()
f = int(f)
i = int(i)
totI = f*12 + i #total height in inches
cen = totI*2.54
met = int(cen//100)
cen = cen - (met*100)
print('Your height in meters and centimeters is:', met, cen)