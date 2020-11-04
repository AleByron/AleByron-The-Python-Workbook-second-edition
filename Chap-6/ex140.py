dict = {'a':'Newfoundland', 'b':'Nova Scotia', 'c':'Prince Edward Island', 'e': 'New Brunswick', 'g': 'Quebec', 'h': 'Quebec', 'j': 'Quebec', 'k':'Ontario', 'l':'Ontario', 'm':'Ontario', 'n':'Ontario', 'p':'Ontario', 'r': 'Manitoba', 's':'Saskatchewan', 't':'Alberta', 'v':'British Columbia', 'x':'Nunavut or Northwest Territories', 'y':'Yukon'}
pc = str(input('Enter a postal code:'))
x = 0
add = ''
if pc[0] in dict:
    add = dict[pc[0]]
    if '1'<= pc[1] <= '9':
        add = add + ' Urban'
    elif pc[1]=='0':
        add = add + ' Rural'
    else:
        add = 'Error, second element is not a digit'
else:
    add = 'Error, first element is not a valid character'

print(add)
