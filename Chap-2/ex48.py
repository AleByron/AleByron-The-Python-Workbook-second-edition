month = str(input('Insert a month:'))
day = int(input('insert a day:'))
month = month.lower()
if month == 'december':
    if 22 <= day <= 31 :
        sign = 'Capricorn'
    elif 1 <= day <= 21:
        sign = 'Sagittarius'
    else:
        sign = 'Something went wrong, retry insert your birthday'
elif month == 'january':
    if 1 <= day <= 19 :
        sign = 'Capricorn'
    elif 20 <= day <= 31:
        sign = 'Aquarius'
    else:
        sign = 'Something went wrong, retry insert your birthday'
elif month == 'february':
    if 1 <= day <= 18 :
        sign = 'Aquarius'
    elif 19 <= day <= 31:
        sign = 'Pisces'
    else:
        sign = 'Something went wrong, retry insert your birthday'
elif month == 'march':
    if 1 <= day <= 20 :
        sign = 'Pisces'
    elif 21 <= day <= 31:
        sign = 'Aries'
    else:
        sign = 'Something went wrong, retry insert your birthday'
elif month == 'april':
    if 1 <= day <= 20 :
        sign = 'Aries'
    elif 21 <= day <= 31:
        sign = 'Taurus'
    else:
        sign = 'Something went wrong, retry insert your birthday'
elif month == 'may':
    if 1 <= day <= 20 :
        sign = 'Taurus'
    elif 21 <= day <= 31:
        sign = 'Gemini'
    else:
        sign = 'Something went wrong, retry insert your birthday'
elif month == 'june':
    if 1 <= day <= 20 :
        sign = 'Gemini'
    elif 21 <= day <= 31:
        sign = 'Cancer'
    else:
        sign = 'Something went wrong, retry insert your birthday'
elif month == 'july':
    if 1 <= day <= 22 :
        sign = 'Cancer'
    elif 23 <= day <= 31:
        sign = 'Leo'
    else:
        sign = 'Something went wrong, retry insert your birthday'
elif month == 'august':
    if 1 <= day <= 22 :
        sign = 'Leo'
    elif 23 <= day <= 31:
        sign = 'Virgo'
    else:
        sign = 'Something went wrong, retry insert your birthday'
elif month == 'september':
    if 1 <= day <= 22 :
        sign = 'Virgo'
    elif 23 <= day <= 31:
        sign = 'Libra'
    else:
        sign = 'Something went wrong, retry insert your birthday'
elif month == 'october':
    if 1 <= day <= 22 :
        sign = 'Libra'
    elif 23 <= day <= 31:
        sign = 'Scorpio'
    else:
        sign = 'Something went wrong, retry insert your birthday'
elif month == 'november':
    if 1 <= day <= 21 :
        sign = 'Scorpio'
    elif 22 <= day <= 31:
        sign = 'Sagittarius'
    else:
        sign = 'Something went wrong, retry insert your birthday'

print(sign)
