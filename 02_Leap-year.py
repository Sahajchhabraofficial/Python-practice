#Write a program to check given year is leap year or not
year=int(input("enter a year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("year is Leap")
else:
    print("year is not Leap")