from ex163 import FreqNames


mex = input('Enter an year:')
male = FreqNames(mex)[0]
female = FreqNames(mex)[1]
both = []
for x in male:
    if x in female and x not in both:
        both.append(x)

print('No gender neames used the year you choosed are:',both)