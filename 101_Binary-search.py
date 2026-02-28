#Write a program to check (search) given number is present or not present in array , using binary search.
lst=[]
for i in range(4):
    ele=int(input("enter a number: "))
    lst.append(ele)
lst.sort()
search=int(input("enter a search integer: "))
first=0
last=len(lst)-1 
print(lst)
while first<=last: 
    m=(first+last)//2 
    if lst[m]==search:
        print("number found")
        break
    elif lst[m]<search:
        first=m+1  
    else:
        last=m-1  
else:
    print("num is not found")