def is_palindrome(text):
    return text==text[::-1]
text=input("Enter a string: ")
print(is_palindrome(text))
