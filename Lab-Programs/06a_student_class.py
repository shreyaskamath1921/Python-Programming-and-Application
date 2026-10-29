class Student:
    def __init__(self,name,srn):
        self.__name=name
        self.__srn=srn
    def display(self):
        print("Name:",self.__name)
        print("SRN:",self.__srn)
srn=input("Enter your SRN: ")
students=[Student("Shreyas Kamath",srn),Student("Rahul","R25EV001")]
for student in students:
    student.display()
