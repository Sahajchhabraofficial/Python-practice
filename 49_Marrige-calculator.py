#Write a Program to accept user’s marital status, gender and age to check if he/she is eligible for marriage or not.
marital_status=input("Enter your marital status: ")
gender=input("Enter your gender: ")
age=int(input("Enter your age: "))
if gender=="male" or gender=="Male" or gender=="MALE":
    if age>=21 and marital_status=='single':
        print("You are eligible for marrige")
    else:
        print("You are not eligible for marrige")
elif gender=="female" or gender=="Female" or gender=="FEMALE":
    if age>=19 and marital_status=='single':
        print("You are eligible for marrige")
    else:
        print("You are not eligible for marrige")
    