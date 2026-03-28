#simple inheritance
class person:
    def set_Person(self,arg1,arg2):
        self.name=arg1
        self.mob=arg2
    def displayPerson(self):
        print("-----Person info-----")
        print("Name: ",self.name)
        print("contact: ",self.mob)
class student(person):
    def __init__(self,id,rno,course):
        self.id=id
        self.rno=rno
        self.course=course
    def displayStudent(self):
        print("-----Student info-----")
        print("id: ",self.id)
        print("Roll no.: ",self.rno)
        print("Course: ",self.course)
        print("---------------------")


obj1=student('CS1247',1125,"B.tech")
obj1.set_Person("Gaurav Sani",6534185160)
obj1.displayPerson()
obj1.displayStudent()