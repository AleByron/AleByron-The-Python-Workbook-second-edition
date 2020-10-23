n= 10
x =0
t =[]
while x < 10:
    x = x+1
    t.append(x*10)

for cels in t:
    far = cels * 1.8 + 32
    print(cels ,'Celsius is equal to', far, 'Fahrenheit')