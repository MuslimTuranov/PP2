import os

path = input()
list = []
for path in os.listdir(path):
    list.append(path)

print(list)
