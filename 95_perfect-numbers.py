#Write a program to count how many elements in an array are perfect and how many are not perfect.
lst=[]
for i in range(4):
    ele=int(input("enter a number: "))
    lst.append(ele)

perfect=[]
notperfect=[]
fact=[]
for num in lst:
    for j in range(1,num+1):
        if num%i==0:
            fact.append(i)
    sum=0
    for k in fact:
        sum+=k
    if sum==num:
        perfect.append(num)
    else:
        notperfect.append(num)
print("perfect numbers: ",perfect)
print("not perfect numbers: ",notperfect)