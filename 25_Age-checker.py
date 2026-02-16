#Write a program to Check whether a person is a child, teenager, adult, or senior based on age.
age=int(input("enter your age: "))
if age>=0 and age<13:
    print("You are a child")
elif age>=13 and age<19:
    print("You are a teenager")
elif age>=19 and age<40:
    print("You are an adult")
elif age>=40 and age<=100:
    print("You are senior")