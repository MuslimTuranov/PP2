import os
import shutil
pathforoldfile = input("enter the path of old file: ")
pathfornewfile = input("enter the path for new file: ")
try:
    with open(pathforoldfile, "r") as oldfile:
        with open(pathfornewfile + '\\' + 'newfile.doc', "w") as newfile:
            shutil.copyfileobj(oldfile, newfile)
except FileNotFoundError:
  print("file not found")