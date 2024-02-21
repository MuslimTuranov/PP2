def generators3(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
n = int(input())

x = generators3(n)

print(','.join(map(str, x)))
