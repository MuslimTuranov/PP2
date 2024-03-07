import os

n = int(input("enter the size of the list: "))
list = []
for i in range(n):
    i = input()
    list.append(i)
text_file = input('enter the path of your txt file: ')
file = open(text_file, "w")
for element in list:
    file.write(element + "\n")