x = float(input('Insert a grade:'))
x = round(x,1)
if x>=4.0:
    g = 'A+'
elif 0 >= round(x-4,1) >= -0.1 :
    g = 'A'
elif -0.2 >= round(x-4,1) >= -0.5:
    g = 'A-'
elif 0.4 >= round(x-3,1) >= 0.2:
    g = 'B+'
elif 0.1 >= round(x-3,1) >= -0.1:
    g = 'B'
elif -0.2 >= round(x-3,1) >= -0.5:
    g = 'B-'
elif 0.4 >= round(x-2,1) >= 0.2:
    g = 'C+'
elif 0.1 >= round(x-2,1) >= -0.1:
    g = 'C'
elif -0.2 >= round(x-2,1) >= -0.5:
    g = 'C-'
elif 0.4 >= round(x-1,1) >= 0.2:
    g = 'D+'
elif 0.1 >= round(x-1,1) >= -0.1:
    g = 'D'
elif -0.2 >= round(x-1,1):
    g = 'F'


print(g)