#Write a program to print cube of all numbers present in a given array.
lst=[]
for i in range(4):
    ele=int(input("Enter elements: "))
    lst.append(ele)

lst2=[ num*num*num for num in lst ]
print(lst2)