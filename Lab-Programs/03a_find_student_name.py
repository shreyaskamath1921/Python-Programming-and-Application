my_name=input("Enter your name: ")
names=[input(f"Enter student {i+1} name: ") for i in range(5)]
print("Your name is present." if my_name.lower() in [name.lower() for name in names] else "Your name is not present.")
