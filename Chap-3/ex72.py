x = 1
while x <= 100:
    if x%3==0 and x%5==0:
        print('Fizz and Buzz')
    elif x%3==0:
        print('Fizz')
    elif x%5==0:
        print('Buzz')
    else:
        print(x)
    x=x+1