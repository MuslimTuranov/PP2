def generators4(a, b):
    for i in range(a , b + 1):
        yield i * i

a = int(input())
b = int(input())

x = generators4(a, b)


for y in x:
    print(y)
        
for i in range(a, b + 1):
    print(i * i)