def unique(n, arr):
    uniquelist = list(dict.fromkeys(arr))
    print(uniquelist)

n = int(input())
arr = []

for i in range(0, n):
    x = int(input())
    arr.append(x)

unique(n, arr)