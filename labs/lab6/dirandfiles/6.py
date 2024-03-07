import os

path = input("enter the path where you want to create new files: ")
list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(1, 27):
    for j in list:
        open(path + "\\" + j + ".txt", "w")