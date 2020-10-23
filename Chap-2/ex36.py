d_age = float(input('Insert your dogs age:'))
if d_age<=2 and d_age>0:
    h_age = d_age*10.5
    print('Your dogs age in human years id equal to:',h_age)
elif d_age>2 and d_age>0:
    h_age = (d_age-2)*4+21
    print('Your dogs age in human years id equal to:', h_age)
else:
    print('The number you inserted is invalid')