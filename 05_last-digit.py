#Write a program to check wether the last digit of number (enter by user) is divisible by 3 or not.
num=int(input("enter a number: "))
last_dig=num%10
if last_dig%3==0:
    print("Last digit is divisible by 3")
else:
    print("Last digit is not divisible by 3")