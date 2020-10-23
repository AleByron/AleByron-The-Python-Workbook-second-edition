
def cleanData(na,x):

    if len(na) < 4:
        res = ('You have to put more elements in your list')

    na.sort()
    for a in range(x):
        na.pop(0)
        na.pop(len(na) - 1)

    return na

def main():
    list =[]
    orlist=[]
    while 0<1:
       a = int(input('Enter a positive integer: '))
       if a == 0:
           break
       list.append(a)

    for i in list:
        orlist.append(i)

    n = int(input('Enter the cleaning value:'))
    print(cleanData(list,n),end = " ")
    print(orlist, end = " ")


main()