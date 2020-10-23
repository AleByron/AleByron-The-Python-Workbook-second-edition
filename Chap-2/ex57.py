min = float(input('How many air minute have you used this month?:'))
mex = int(input('How many messages have you used this month?:'))
base_tar = 15.00
emer_tar = 0.44
min_tar = 0
mex_tar = 0

if min > 50:
    min_tar = (min - 50)*0.25
if mex > 50:
    mex_tar = (mex - 50)*0.15

tot = (base_tar+emer_tar+min_tar+mex_tar)+((base_tar+emer_tar+min_tar+mex_tar)*5/100)
print(tot)

