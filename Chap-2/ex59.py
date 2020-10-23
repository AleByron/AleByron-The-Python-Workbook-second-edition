date = str(input('Insert a date as in the example (ex. 2019-01-01):'))
y = int(date[0:4])
m = int(date[5:7])
d = int(date[8:10])
if m == 1:
    if d<31:
        da=d+1
    else:
        da = 1
        m = 2
elif m == 2:
    if y % 400 == 0:
        if d<29:
            da = d+1
        else:
            da = 1
            m=3
    elif y % 100 == 0:
        if d<28:
            da = d+1
        else:
            da=1
            m=3
    elif y%4==0:
        if d<29:
            da = d+1
        else:
            da = 1
            m = 3
    else:
        if d<28:
            da = d+1
        else:
            da = 1
            m = 3
elif m == 3:
    if d<31:
        da=d+1
    else:
        da = 1
        m = 4
elif m == 4:
    if d<30:
        da=d+1
    else:
        da = 1
        m = 5
elif m == 5:
    if d<31:
        da=d+1
    else:
        da = 1
        m = 6
elif m == 6:
    if d<30:
        da=d+1
    else:
        da = 1
        m = 7
elif m == 7:
    if d<31:
        da=d+1
    else:
        da = 1
        m = 8
elif m == 8:
    if d<31:
        da=d+1
    else:
        da = 1
        m = 9
elif m == 9:
    if d<30:
        da=d+1
    else:
        da = 1
        m = 10
elif m == 10:
    if d<31:
        da=d+1
    else:
        da = 1
        m = 11
elif m == 11:
    if d<30:
        da=d+1
    else:
        da = 1
        m = 12
elif m == 12:
    if d<31:
        da=d+1
    else:
        da = 1
        m = 1
        y = y+1


print("%02d" % y,"%02d" % m, "%02d" % da)