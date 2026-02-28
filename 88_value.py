#Write a program that accepts some integers from the user and finds the highest value and the input position.
lst=[]
for i in range(4):
    ele=int(input("enter elements: "))
    lst.append(ele)
maxi=lst[0]
for j,k in enumerate(lst):
    if k<maxi:
        maxi=lst[j]
print("maximum element with logic: ",k,"index: ",j)