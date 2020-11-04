dict =  {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
dictd =  {'0':'zero', '1':'ten', '2':'twelve', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}
amount=str(input('Enter an integer for an amount:'))
x = len(amount)

lit = ''
if x == 1:
    lit = dict[amount[0]]
elif x == 2:
    lit = dictd[amount[0]] + ' ' + dict[amount[1]]
elif x == 3:
    lit = dict[amount[0]] + ' hundred ' + dictd[amount[1]] + ' ' + dict[amount[2]]

print(lit)