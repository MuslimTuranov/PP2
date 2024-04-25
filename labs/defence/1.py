import re

number = input()

pattern = r'([+7]|[8])777.{8}|([+7]|[8])705.{8}'

if re.search(pattern, number):
    print("beeline")
else:
    print("not")
