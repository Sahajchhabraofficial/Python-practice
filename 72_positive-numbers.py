#Write a program to display all positive numbers present in an array
lst=[]
for i in range(4):
    ele=int(input("Enter a number: "))
    lst.append(ele)
for  j in range(4):
    if lst[j]>0:
        print(lst[j])
        