import re

pattern = r'ab*'
with open('row.txt', 'r') as file:
    for line in file:
        if re.search(pattern, line):
            print(line.strip())
