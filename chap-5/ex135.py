n = int(input('Enter an int:'))
a = 0
b = 1
primes = []
realp= []
p = 2
while n>=a:
    primes.append(a)
    a = a+1

primes[1] = 0

while p<n:
    for i in range(p*2, n+1, p):
        primes[i] = 0
    p = p+1
    while p < n and primes[p] == 0:
        p = p+1

a = 0
while len(primes)>a :
    if primes[a] != 0:
        realp.append(primes[a])
    a = a+1

print(realp)


