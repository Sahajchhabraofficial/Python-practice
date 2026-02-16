#Given a month number, print the number of days (with Feb as 28 days).
month=int(input("Enter a month number: "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("Number of days= 31")
elif month==2:
    print("number of days= 28")
elif month>1 and month<12:
    print("number of days 30")
else:
    print("There are only 12 months")