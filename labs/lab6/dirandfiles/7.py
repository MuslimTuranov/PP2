import os
import shutil

oldfile = input("old: ")
newfile = input("new: ")

try:
    with open(oldfile, "r") as oldfile:
        with open(newfile, "w") as newfile:
            shutil.copyfileobj(oldfile, newfile)
except FileNotFoundError:
    print("File not found")
