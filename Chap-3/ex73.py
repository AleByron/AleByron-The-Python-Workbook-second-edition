m = str(input('Enter your message:'))
s = int(input('Enter the shift value:'))
nm = str('') #New message
if s>26 or s<-26: #Check if shift value is valid, elif make it valid
    s= s%26

for x in m:
    if 'a' <= x <= 'z' or 'A' <= x <= 'Z': #check if it's a letter of not
        x1 = (chr(ord(x)+s))
        if 'a' <= x1 <= 'z' or 'A' <= x1 <= 'Z':  #check if the result is still a letter
            x1 = x1
        else: #if the result it's not a letter, make it a letter
            x1 = (chr(ord(x)-26+s))
    else: #values that are not letters must stay the same
        x1 = x
    nm = nm + x1

print(nm)