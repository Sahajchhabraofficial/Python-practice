#Write a program to take array elements from the user, add 5 to each element, store the results in a new array, and display the new array.
lst=[]
for i in range(4):
    ele=int(input("enter elements: "))
    lst.append(ele)
newlist=[num+5 for num in lst]
print("new list: ",newlist)
