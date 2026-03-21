def PrintName(name,gender):
    if gender=="Male":
        print(f"Hello Mr.{name}")
    elif gender=="Female":
        print(f"Hello Mis.{name}")
    else:
        print(f"Hello {name}")

nam=input("enter you name: ")
gen=input("Enter your gender: ")
PrintName(nam,gen)