#Write a program to check how many digits at each index of array.
lst=[]
for i in range(4):
    ele=(input("enter a num: "))
    lst.append(ele)
print((lst))
digitlst=[]
for num in lst:
    digitlst.append(len(num))

print("digit list: ",digitlst)