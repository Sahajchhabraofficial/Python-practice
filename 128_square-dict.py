#wap to store the number in the dictionary as a key and square as its value.
number=int(input("Enter a range: "))
square={}
for i in range(1,number+1):
    square[i]=i*i
print(square)