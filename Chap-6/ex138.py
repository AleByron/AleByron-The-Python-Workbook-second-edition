dic = {1:['.','\,','?','!','\:'], 2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z'], 0:' '}

mess = str(input('Insert your message:'))
mess.lower()
x = 0
y = 0
n = []
for i in mess:
    while x < 10:
        if i in dic[x]:
            if i == dic[x][0]:
                n.append(x)
            else:
                n.append(x)
                while i != dic[x][y]:
                    if x != []:
                        n.append(x)
                    y = y + 1
        x = x+1
    x = 0
    y = 0

print(n)

