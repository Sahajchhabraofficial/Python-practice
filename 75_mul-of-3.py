#Write a program to display all elements in an array that are multiples of 3
lst=[]
for i in range(4):
    ele=int(input("Enter list elements: "))
    lst.append(ele)
for j in range(4):
    if lst[j]%3==0:
        print(lst[j])