#Write a program to count how many elements in an array are divisible by 3,5, and 8.
lst=[]
for i in range(4):
    ele=int(input("enter array elements: "))
    lst.append(ele)
count=0
for num in lst:
    if num%3==0 and num%5==0 and num%8==0:
        count+=1
print(f"there are {count} elements which are divisible by 3,5,8")