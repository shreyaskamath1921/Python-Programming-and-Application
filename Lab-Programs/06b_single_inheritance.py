class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Student(Person):
    def __init__(self,name,age,srn,college):
        super().__init__(name,age)
        self.srn=srn
        self.college=college
    def display(self):
        super().display()
        print("SRN:",self.srn)
        print("College:",self.college)
srn=input("Enter your SRN: ")
student=Student("Shreyas Kamath",19,srn,"REVA University")
student.display()
