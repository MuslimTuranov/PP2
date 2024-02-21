def generators2(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
    
n = int(input())

evens = generators2(n)

print(','.join(map(str, evens)))