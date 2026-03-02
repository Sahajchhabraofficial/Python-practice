#Write a program to check given array is sorted or not.
lst=[]
for i in range(4):
    ele=int(input("Enter a number: "))
    lst.append(ele)
sortedlst=lst.copy()
sortedlst2=lst.copy()
sortedlst.sort()
sortedlst2.sort(reverse=True)
if lst==sortedlst or lst==sortedlst2:
    print("List is sorted!")
else:
    print("List is not sorted!")