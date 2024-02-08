def prime_filter(lst):
    primes = []
    for n in lst:
        isprime = True
        for i in range(2, (n//2)+1):
            if n % i == 0:
                isprime = False
                break
        if isprime:
            primes.append(n)
    print(primes)
                

lst = []

n = int(input())

for i in range(0, n):
    x = int(input())
    lst.append(x)

prime_filter(lst)