#Write a program to input all sides of a triangle and check whether triangle is valid or not.
s1=int(input("enter side 1:"))
s2=int(input("enter side 2: "))
s3=int(input("enter side 3: "))
if s1==s2==s3 or s1==s2!=s3 and s1!=s2==s3 or s1!=s2!=s3:
    print("Triangle is valid")
else:
    print("Triangle is not valid")
