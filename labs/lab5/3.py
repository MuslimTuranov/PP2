import re

pattern = r'[a-z]+\_'
with open(r"C:\Users\musli\Documents\pp2\PP2\labs\row.txt", 'r', encoding='utf-8') as file:
    for line in file:
        if re.search(pattern, line):
            print(line.strip())