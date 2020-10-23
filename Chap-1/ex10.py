import math
a = int(input("enter an integer a: "))
b = int(input("enter an integer b: "))
sum = a+b
diff = b-a
prod = a*b
quot = float(a/b)
rem = float(math.remainder(a, b))
logar = math.log10(a)
pow = a**b
print("sum= ", sum)
print("diff= ", diff)
print("prod= ", prod)
print("quot= ", quot)
print("rem= ", rem)
print("logar= ", logar)
print("pow= ", pow)