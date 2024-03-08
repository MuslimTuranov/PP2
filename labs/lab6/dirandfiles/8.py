import os

path = input("path: ")
if os.access(path, os.F_OK):
    os.remove(path)
else:
    print('the path not found')