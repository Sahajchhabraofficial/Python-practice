#Write a program to accept roll no and marks of 5 subjects of a student, if individuals subject have above 40 marks so print student qualify exam otherwise print student fail in exam and if student qualify exam so Calculate percentage got in exam by student.
# a. If per greater than or equal to 75  A grade
# b. If per between 60-75  B grade
# c. If per between 50-60  C grade
# d. If per between 40-50  D grade
per=int(input("Enter your percentage: "))
if per>=33:
    if per>=75:
        print("Grade A")
    elif per>=60 and per<75:
        print("Grade B")
    elif per>=50 and per<60:
        print("Grade C")
    elif per>=40 and per<50:
        print("Grade D")
else:
    print("Student has faied this exam")