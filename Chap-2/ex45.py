month = str(input('Insert a month:'))
day = str(input('insert a day:'))
date = month+' '+day
date = date.lower()
if date == 'january 1':
    holiday = 'It is New Year’s Day'
elif date == 'july 1':
    holiday = 'It is Canada Day'
elif date == 'december 25':
    holiday = 'It is Christmas Day'
else:
    holiday = 'No holiday this day, go back to work'

print(holiday)
