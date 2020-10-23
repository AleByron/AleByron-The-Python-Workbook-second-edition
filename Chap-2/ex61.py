x = str(input('Enter your license plate:'))

if len(x)==6:
    l = x[0:3]
    n = x[3:6]
    n = int(n)
    if 'A' <= l[0] <= 'Z' and 'A' <= l[1] <= 'Z' and 'A' <= l[2] <= 'Z' and 0 <= n <= 999:
        print('It is an old type license plate')
elif len(x)==7:
    l = x[0:4]
    n = x[4:7]
    if 'A' <= l[0] <= 'Z' and 'A' <= l[1] <= 'Z' and 'A' <= l[2] <= 'Z' and 'A' <= l[3] <= 'Z' and 0 <= n <= 999:
        print('It is an new type license plate')
else:
    print('This license plate is invalid')
print(l,n)
