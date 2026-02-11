#Write a program to print difference between area of two circle but ensure that result must be positive.
r1=int(input("enter radius of circle 1: "))
r2=int(input("enter radius of circle 2: "))
area1=3.14*r1*r1
area2=3.14*r2*r2
if area1>area2:
    print("Difference in area is: ",int(area1-area2))
else:
    print("Difference in area is: ",int(area2-area1))