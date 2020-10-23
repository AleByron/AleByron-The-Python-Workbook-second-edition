rate = float(input('Insert a rating:'))
rate = round(rate,1)
rai = rate*2400
if rate == 0:
    perf = 'unacceptable performance'
    print('This employee had a', perf, 'and its salary raise worth:', rai)
elif rate == 0.4:
    perf = 'acceptable performance'
    print('This employee had a', perf, 'and its salary raise worth:', rai)
elif rate >= 0.6:
    perf = 'meritorious performance'
    print('This employee had a', perf, 'and its salary raise worth:', rai)
else:
    print('You inserted a wrong rate')

