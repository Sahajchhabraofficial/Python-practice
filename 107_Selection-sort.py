#Write a program to arrange (sort) array elements using Selection Sort.
lst=[]
for i in range(5):
    ele=int(input("enter a number: "))
    lst.append(ele)
maximum=lst[0]
index=0
for num in lst:
    if maximum<num:
        maximum=num
    lst[index]= maximum
    index+=1
    maximum=lst[index]
print("sorted list: ",lst)
    
