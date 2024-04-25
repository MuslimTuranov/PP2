import re

def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

with open(r'C:\Users\musli\Documents\pp2\PP2\labs\row.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(camel_to_snake(line.strip()))