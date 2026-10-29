def count_vowels(text):
    return sum(1 for char in text.lower() if char in "aeiou")
text=input("Enter a string: ")
print("Number of vowels:",count_vowels(text))
