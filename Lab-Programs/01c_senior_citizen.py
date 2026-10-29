from datetime import date
name=input("Enter the name: ")
birth_year=int(input("Enter the year of birth: "))
age=date.today().year-birth_year
print(f"{name} is a senior citizen." if age>=60 else f"{name} is not a senior citizen.")
