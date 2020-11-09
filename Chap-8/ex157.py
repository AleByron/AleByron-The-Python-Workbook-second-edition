

x = str(input('Insert a grade:'))
while x != '':
    try:
        if x == 'A+':
            g = 4.0
        elif x == 'A':
            g = 4.0
        elif x == 'A-':
            g = 3.7
        elif x == 'B+':
            g = 3.3
        elif x == 'B':
            g = 3.0
        elif x == 'B-':
            g = 2.7
        elif x == 'C+':
            g = 2.3
        elif x == 'C':
            g = 2.0
        elif x == 'C-':
            g = 1.7
        elif x == 'D+':
            g = 1.3
        elif x == 'D':
            g = 1.0
        elif x == 'F':
            g = 0
        else:
            try:
                x = int(x)
                x = round(x, 1)
                if x >= 4.0:
                    g = 'A+'
                elif 0 >= round(x - 4, 1) >= -0.1:
                    g = 'A'
                elif -0.2 >= round(x - 4, 1) >= -0.5:
                    g = 'A-'
                elif 0.4 >= round(x - 3, 1) >= 0.2:
                    g = 'B+'
                elif 0.1 >= round(x - 3, 1) >= -0.1:
                    g = 'B'
                elif -0.2 >= round(x - 3, 1) >= -0.5:
                    g = 'B-'
                elif 0.4 >= round(x - 2, 1) >= 0.2:
                    g = 'C+'
                elif 0.1 >= round(x - 2, 1) >= -0.1:
                    g = 'C'
                elif -0.2 >= round(x - 2, 1) >= -0.5:
                    g = 'C-'
                elif 0.4 >= round(x - 1, 1) >= 0.2:
                    g = 'D+'
                elif 0.1 >= round(x - 1, 1) >= -0.1:
                    g = 'D'
                elif -0.2 >= round(x - 1, 1):
                    g = 'F'
            except ValueError:
                print('Something went wrong, retry')
                g = ''
        print(g)
    except ValueError:
        print('Something went wrong, retry')
    x = str(input('Insert a grade:'))


