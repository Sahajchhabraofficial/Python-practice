#Write a program to input elements into an array and divide them into two separate arrays — one containing prime numbers and the other containing not prime numbers.
lst=[]
prime=[]
notprime=[]
for i in range(4):
    ele=int(input("enter elements: "))
    lst.append(ele)

for i in range(4):
    count=0
    for j in range(1,lst[i]+1):
        if lst[i]%j==0:
            count+=1
    if count==2:
        prime.append(lst[i])
    else:
        notprime.append(lst[i])
print("prime list: ",prime)
print("not prime list: ",notprime)