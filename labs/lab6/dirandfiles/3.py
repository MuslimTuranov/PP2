import os

path = input()

if os.path.exists(path):
    print("The path exists")
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print("Filename:", filename)
    print("Directory:", directory)
else: 
    print("The path does not exist")