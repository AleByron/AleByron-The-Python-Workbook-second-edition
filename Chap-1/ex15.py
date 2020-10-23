feets = float(input('Insert the distance in feets:' ))


miles = feets//5280
yard = (feets-miles*5280)//3
feets1 = (feets-miles*5280-yard*3)//1
inches = (feets-miles*5280-yard*3-feets1)*12

print('the distance is:', miles,'miles', yard,'yards', feets1,'feets', inches, 'inches')
