#Write a program to interchange first and last elements in an array
lst=[]
for i in range(4):
    ele=int(input("enter elements: "))
    lst.append(ele)
temp=lst[0]
lst[0]=lst[-1]
lst[-1]=temp
print("after interchange: ",lst)