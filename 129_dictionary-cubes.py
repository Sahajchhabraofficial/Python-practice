#wap to store a number as a key in a dictionary and its cube as its value.
number=int(input("Enter a range: "))
cube={}
for i in range(1,number+1):
    cube[i]=i*i*i

print(cube)