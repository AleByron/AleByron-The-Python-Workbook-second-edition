q = int(input('Enter a decimal number:'))
res = ''
while q != 0:
    r = q % 2
    r = str(r)
    res = res + r
    q = q // 2
c = len(res)
counter = -1
res_new = ''
for x in res:
    counter = counter + 1
    d = c - counter
    e = c - counter - 1
    f = res[e:d]
    res_new = res_new + f


print('The number you entered in decimal is',res_new,'in binary')
