#Write a program to reverse all elements of an array without using any extra array
lst=[]
for i in range(4):
    ele=int(input("enter a number: "))
    lst.append(ele)

copylst=lst[::-1]
print("reversed another list: ",copylst)