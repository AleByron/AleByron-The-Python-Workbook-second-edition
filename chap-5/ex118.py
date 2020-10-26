from ex117 import splitWords

x = str(input('Enter a string:'))
x = x.lower()
list = splitWords(x)
revlist = splitWords(x)
revlist.reverse()

a = False
if list==revlist:
    a = True

else:
    a = False

print(a,revlist,list)
