#Write a program to find the maximum element in an array.
lst=[]
for i in range(4):
    ele=int(input("enter elements: "))
    lst.append(ele)
print("maximum element with method: ",max(lst))
maxi=lst[0]
for j in range(4):
    if maxi<lst[j]:
        maxi=lst[j]
print("maximum element with logic: ",maxi)