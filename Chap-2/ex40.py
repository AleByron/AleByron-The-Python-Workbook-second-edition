x = float(input('Insert a noise value in db:'))
if x == 130:
    print('It is a Jackhammer')
elif x == 106:
    print('It is a Gas Lawnmower')
elif x ==  70:
    print('It is an Alarm Clock')
elif x == 40:
    print('Its a Quiet Room')
elif 70 > x > 40:
    print('It is between a quite room and an alarm clock')
elif 106 > x > 70:
    print('It is between an alarm clock and a gas lawnmower')
elif 130 > x > 106:
    print('It is between a gas lawnmower and a jackhammer')
elif x > 130:
    print('It is louder than a Jackhammer')
else:
    print('It is quieter than a quiet room')