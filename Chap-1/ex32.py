n = int(input('Insert a 4 four digit number:'))
n1 = int(str(n)[:-3])
n2 = int(str(n)[:-2])-(n1*10)
n3 = int(str(n)[:-1])-int(str(n)[:-2])*10
n4 = n - (int(str(n)[:-1])*10)
sum = n1+n2+n3+n4
print(n1,'+', n2,'+', n3,'+', n4,'=',sum)