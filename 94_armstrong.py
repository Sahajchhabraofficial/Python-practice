#Write a program to count how many elements in an array are armstrong and how many are not armstrong.
lst=[]
for i in range(4):
    ele=int(input("enter a number: "))#153
    lst.append(ele)
arm=[]
notarm=[]
for num in lst:
    length=len(num)
    first=num//100
    second=(num%100)//10
    third=(num//10)%10
    first=first**length
    second=second**length
    third=third**length
    sum=first+second+third
    if sum==num:
        arm.append(num)
    else:
        notarm.append(num)
print("Armstrong numbers: ",arm)
print("Not armstrong: ",notarm)