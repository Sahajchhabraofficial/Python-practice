#Write a program to read the age of a candidate and determine whether he is eligible to cast his/her own vote in india or not.
age=int(input("Enter your age: "))
country=input("Enter your country: ")
if country=="india" or country=="INDIA" or country=="India":
    if age>=18:
        print("You are eligible to cast vote in india")
    else:
        print("Your are not eligible to cast vite in india")
else:
    print("This website is for indian people only!")