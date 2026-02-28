#Write a program to input elements into an array and divide them into two separate arrays — one containing even numbers and the other containing odd numbers.
lst=[]
for i in range(4):
    ele=int(input("Enter numbers: "))
    lst.append(ele)
even=[]
odd=[]
for i in range(4):
    if lst[i]%2==0:
        even.append(lst[i])
    else:
        odd.append(lst[i])

print("even list: ",even)
print("odd list: ",odd)