#Write a program to find the minimum element in an list.
lst=[]
for i in range(4):
    ele=int(input("Enter elements: "))
    lst.append(ele)
print("minimum element wit function: ",min(lst))
mini=lst[0]
for j in range(4):
    if mini>lst[j]:
        mini=lst[j]
print("minimum element with logic: ",mini)