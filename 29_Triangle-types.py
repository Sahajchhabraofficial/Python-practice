#Check whether the triangle is equilateral, scalene, or isosceles.
s1=int(input("Enter side 1:  "))
s2=int(input("Enter side 2: "))
s3=int(input("Enter side 3: "))
if s1+s2>s3 and s2+s3>s1 and s3+s1>s2:
    if s1==s2==s3:
        print("it is a equilatiral triangle")
    elif s1==s2!=s3 or s1!=s2==s3:
        print("it is a isoselus triangle")
    elif s1!=s2!=s3:
        print("it is a scalene triangle")
else:
    print("Triangle is not valid")