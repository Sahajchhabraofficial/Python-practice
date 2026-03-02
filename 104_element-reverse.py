#Write a program to reverse the digits of every element present in an array.
lst=[]# [12,34,56,78]
for i in range(4):
    ele=int(input("enter a number: "))
    lst.append(ele)
revlst=[]
print("original list: ",lst)
for num in lst:
    first=num//10
    last=num%10
    #print(last,end="")
    #last=num%10
    #print(first,end="")
    #print()
    revele=str(last)+str(first)
    revlst.append(int(revele))
print("Reversed list: ",revlst)
    