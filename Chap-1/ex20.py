P = float(input('Define the pressure of gas in Pascal:'))
V = float(input('Define the volume of gas in liters:'))
T = float(input('Define the Temperature of gas in celsius degrees:'))
R = 8.314 #e ideal gas constant, equal to 8.314 J/(n*K)
T = T + 273.15 #celsius to kelvin
n = (P*V)/(R*T)
print('the number of moles in your tank is:',n)