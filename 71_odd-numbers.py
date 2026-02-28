#Write a program to display all odd numbers present in an array
lst=[]
for i in range(4):
    ele=int(input("enter list elements: "))
    lst.append(ele)
for j in range(4):
    if lst[j]%2==1  :
        print(lst[j])
