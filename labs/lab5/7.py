def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

with open(r"C:\Users\musli\Documents\pp2\PP2\labs\row.txt", 'r', encoding='utf-8') as file:
    for line in file:
        print(snake_to_camel(line.strip()))
