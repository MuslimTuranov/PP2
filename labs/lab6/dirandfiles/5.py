import os

n = int(input())
lst = []
for i in range(n):
    x = input()
    lst.append(x)

text_file = input('path: ')
with open(text_file, "w") as file:
    for element in lst:
        file.write(element + "\n")
