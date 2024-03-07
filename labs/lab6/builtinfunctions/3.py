s = input()

g = s[::-1]

m = ''.join(reversed(s))

if s == m:
    print("Palindrome")
else:
    print("Not")