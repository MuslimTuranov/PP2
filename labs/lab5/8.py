import re

pattern = r'[A-Z][a-z]*'
with open(r"C:\Users\musli\Documents\pp2\PP2\labs\row.txt", 'r', encoding='utf-8') as file:
    for line in file:
        print(re.findall(pattern, line.strip()))