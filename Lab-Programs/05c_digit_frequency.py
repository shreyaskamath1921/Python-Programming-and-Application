number=input("Enter a multi-digit number: ")
for digit in sorted(set(number)):
    if digit.isdigit():
        print(f"Frequency of {digit}: {number.count(digit)}")
