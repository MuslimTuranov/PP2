def generators5(n):
    for i in range(n + 1):
        yield i

n = int(input())

numbers = generators5(n)

reversenumbers = reversed(list(numbers))

print(','.join(map(str, reversenumbers)))
