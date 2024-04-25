import re

def insert_spaces(text):
    # Use regular expression to insert spaces before words starting with capital letters
    modified_text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return modified_text

# Example usage:
input_text = "ThisIsAExampleStringWithWordsStartingWithCapitalLetters"
result = insert_spaces(input_text)
print(result)
