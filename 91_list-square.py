#Write a program to take array elements from the user, store their squares in a new array, and display the new array.
lst=[]
newlist=[]
for i in range(4):
    ele=int(input(("enter elements: ")))
    lst.append(ele)

newlist=[num*num for num in lst]
print("square list: ",newlist)

