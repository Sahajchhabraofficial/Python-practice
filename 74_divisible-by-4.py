#Write a program to display all elements in an array that are divisible by 4.
lst=[]
for i in range(4):
    ele=int(input("Enter a element: "))
    lst.append(ele)

for j in range(4):
    if lst[j]%4==0:
        print(lst[j])