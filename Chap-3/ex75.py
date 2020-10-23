a = str(input('Enter a string:'))
b = []#array of chars
c = len(a)
for x in a:
    b.append(x)

d=0 #counter of the loop
e = 0 #to check if the sting is palindrome
for x in b:
    if x == b[c-d-1]:
        d = d+1
        e = e
    else:
        e = e+1

if e==0:
    print('The string is palindrome')
else:
    print('The string is not palindrome')
