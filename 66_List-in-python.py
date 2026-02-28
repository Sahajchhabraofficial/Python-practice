#Write a program to input and print all elements of an array.
lst=[]
for i in range(4):
    lnp=int(input(f"Enter {i+1} integer values of a list: "))
    lst.append(lnp)
print(lst)