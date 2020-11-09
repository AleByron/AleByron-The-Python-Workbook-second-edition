from ex163 import FreqNames

st_date = input('Enter a starting date:')
fn_date = input('Enter a final date:')

male = {}
female = {}

for date in range(int(st_date),int(fn_date)+1):
    date = str(date)
    male.setdefault(date, [])
    x = FreqNames(date)[0]
    male[date].append(x)
    female.setdefault(date, [])
    y = FreqNames(date)[1]
    female[date].append(y)

print('In the period selected the most common male names were:',male)
print('In the period selected the most common female names were:',female)

