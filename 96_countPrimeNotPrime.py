#Write a program to count how many elements in an array are prime and how many are not prime.
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
primecount=len(prime)
notprimecount=len(notprime)
print(f"there are {primecount} numbers which are prime")
print(f"there are {notprimecount} numbers which are not prime")