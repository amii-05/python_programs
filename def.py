class Student:
    name="Rahul"
    age=20
    def marks(self):
        print("Tamil: 89,English: 90")
s1=Student()
print(s1.name)
print(s1.age)
s1.marks()


class student:
    name="unknow"
    mark=0

    def display(self):
        print("name: ",self.name)
        print("mark: ",self.mark)

s1=student()
s1.name="Navisha"
s1.mark=90
s2=student()
s2.name="Nabba"
s2.mark=89
s3=student()
s3.name="Nala"
s3.mark=40
s1.display()
s2.display()
s3.display()

class student:
    name="unknown"
    mark=0
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def setdetails (self,name,mark):
        self.name=name
        self.mark=mark
    def display(self):
        print("name: ",self.name)
        print("mark: ",self.mark)

s1=student("naveen",89)
s1.setdetails("praveena",67)
s1.display()
