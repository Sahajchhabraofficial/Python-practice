#Write a program to display the array elements in reverse orde
lst=[]
for i in range(4):
    ele=int(input("enter elements: "))
    lst.append(ele)

print("reversed list: ",lst[::-1])