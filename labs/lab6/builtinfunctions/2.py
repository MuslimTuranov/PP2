s = input()

countupper = 0
countlower = 0

for i in s:
    if i.isupper() == True:
        countupper += 1
    if i.islower() == True:
        countlower += 1
        
print(f"Uppercase letter: {countupper}")
print(f"Lowercase letter: {countlower}")

