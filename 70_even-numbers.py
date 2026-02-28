#Write a program to display all even numbers present in an array
lst=[]
for i in range(4):
    ele=int(input("enter list elements: "))
    lst.append(ele)
for j in range(4):
    if lst[j]%2==0:
        print(lst[j])
