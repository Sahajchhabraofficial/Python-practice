#Write a program to input elements into an array and divide them into two separate arrays — one containing positive numbers and the other containing nagative numbers.
lst=[]
pos=[]
neg=[]
for i in range(4):
    ele=int(input("enter elements: "))
    lst.append(ele)

for i in range(4):
    if lst[i]>0:
        pos.append(lst[i])
    else:
        neg.append(lst[i])

print("Positive elements: ",pos)
print("negative element: ",neg)