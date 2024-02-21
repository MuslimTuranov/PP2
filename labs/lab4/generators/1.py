def generators1(n):
    for i in range(n + 1):
        yield i * i
    
n = int(input())
squares = generators1(n)

print(','.join(map(str, squares)))