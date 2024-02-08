def palindrome(a):
    b = a[::-1]
    if a == b:
        print("It is a palindrome")
    else:
        print("It is NOT a palindrome")
    

a = input()
palindrome(a)
