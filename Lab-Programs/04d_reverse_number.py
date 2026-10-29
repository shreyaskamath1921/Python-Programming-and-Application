def reverse_number(number):
    sign=-1 if number<0 else 1
    return sign*int(str(abs(number))[::-1])
number=int(input("Enter a number: "))
print("Reversed number:",reverse_number(number))
