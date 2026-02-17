#Write a program using switch-case that takes a roll number as input and prints a dummy result sheet (like name, subject marks, and result) for the student.
roll=int(input("enter your roll number: "))
match roll:
    case 1120:
        print("Name: Sahaj Chhabra")
        print("Subject marks: 79%")
        print("Result: pass")
    case 1121:
        print("Name Gurjot singh gill")
        print("Subject marks: 84%")
        print("Result: pass")
    case 1122:
        print("Name: Kuldeep Meena")
        print("Subject marks: 30%")
        print("Result fail")
    case _:
        print("Student not in school!")