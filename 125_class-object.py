class Super:
    def __init__(self,arg1,arg2):
        self.name=arg1
        self.Phone=arg2
    def display(self):
        print("-----Person info-----")
        print("Name: ",self.name)
        print("Phone: ",self.Phone)
class Sub(Super):
    def __init__(self,arg1,arg2,arg3,arg4):
        super().__init__(arg1,arg2)
        self.section=arg3
        self.rollno=arg4
    def display(self):
        super().display()
        print("-----Student info-----")
        print("Section: ",self.section)
        print("Roll No: ",self.rollno)

std1=Sub("John",1234567890,"A",104)
std1.display()
std2=Sub("Alice",9876543210,"B",202)
std2.display()