s = int(input('Insert a period in seconds:'))

m = s//60
h = m//60
d = h//24
s = s - (m*60)
m = m - (h*60)
h = h - (d*24)
print("The period in second is", "%d:%02d:%02d:%02d." % (d, h, m, s))