def count_digits(text):
    return sum(1 for char in text if char.isdigit())
text=input("Enter a string: ")
print("Number of digits:",count_digits(text))
