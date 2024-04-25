import math

def isprime(x):
    for i in range(2, math.ceil(x/2)):
        if x % i == 0:
            return False
    return True
        

def generator5(x):
    for i in range(2, x + 1):
        if isprime(i):
            yield i

x = int(input())

primes = generator5(x)

print(' '.join(map(str, primes)))





