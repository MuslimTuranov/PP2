def reverse_sentence(s1):  
    words = s1.split()
    reversedwords = reversed(words)
    s2 = " ".join(reversedwords)
    print(s2)

s1 = input()

reverse_sentence(s1)

