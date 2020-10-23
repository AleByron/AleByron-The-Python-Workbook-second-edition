P = float(input('Insert pressure in Kg/Pascal:'))
psi= 0.1450377377*P
mmhg= P/0.1333223684
at= P*0.00986923
print('The pressure in PSI is', psi, 'in mmhg is', mmhg,'and in at is', at)