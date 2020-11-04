def pal(x):
    res = ''
    if len(x)<=1:
        return True
    elif x[0] == x[len(x)-1]:

        x = x[1:len(x)-1]
        pal(x)
        return True
    else:
        return False



def main():
    x = str(input('Enter a string:'))
    print('Is the string palindrome?',pal(x))

main()