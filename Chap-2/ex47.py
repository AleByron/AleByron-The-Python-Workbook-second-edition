month = str(input('Insert a month:'))
day = int(input('insert a day:'))
month = month.lower()
if month == 'january' or month == 'february':
    season = 'winter'
elif month == 'march' and day <= 19:
    season = 'winter'
elif month == 'december' and day >= 21:
    season = 'winter'
elif month == 'april' or month == 'may':
    season = 'spring'
elif month == 'june' and day <= 20:
    season = 'spring'
elif month == 'march' and day >= 20:
    season = 'spring'
elif month == 'july' or month == 'august':
    season = 'summer'
elif month == 'september' and day <= 21:
    season = 'summer'
elif month == 'june' and day >= 22:
    season = 'summer'
elif month == 'october' or month == 'november':
    season = 'spring'
elif month == 'september' and day <= 22:
    season = 'fall'
elif month == 'december' and day >= 20:
    season = 'fall'

#Qui mancherebbero le condizioni di esistenza, ma l'esercizio non le chiede, per cui vengono considerate valide anche date come 'january 8765'
print(season)

