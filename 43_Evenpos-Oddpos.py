#Check if a number is even-positive, even-nagative ,odd-positive ,odd-nagative or zero.
num=int(input("Enter a number :"))
if num!=0:
    if num>0:
        if num%2==0:
            print("Number is Even positive")
        else:
            print("Number is odd positive")
    else:
        if num%2==0:
            print("Number is Even Negative")
        else:
            print("Number is odd Negative")
else:
    print("number is zero")