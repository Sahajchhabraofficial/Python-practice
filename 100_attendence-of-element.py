#Write a program to check (search) given number is present or not present in array , using Linear search.
lst=[]
for i in range(4):
    ele=(input("enter elements: "))
    lst.append(ele)
search=(input("enter search element: "))
if search in lst:
    print("number found")
else:
    print("number not found")