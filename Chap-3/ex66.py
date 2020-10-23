pur = str(input('Insert a purchase value:'))

sum = 0

while pur != "":
    pur = float(pur)
    sum = sum+pur
    pur = str(input('Insert a purchase value:'))

rest = sum - round(sum,1)
rest = round(rest,2)
real = sum
sum = round(sum, 1)
if 0.01 <= rest <= 0.02:
    sum = sum - 0.05
elif 0.03 <= rest <= 0.07:
    sum = sum+0.05
elif 0.08 <= rest <= 0.09:
    sum = sum + 0.1

cash = round(sum,2)
real = round(real,2)
print('The amount in cash is: %.2f' % cash)
print('The real amount is: %.2f' %real)


