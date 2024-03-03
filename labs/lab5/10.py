import re

def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

with open('text.txt', 'r') as file:
    for line in file:
        print(camel_to_snake(line.strip()))