#Write a program to check whether a key exists in dictionary or not.
dict1={23:354,32:432,23:565}
search=int(input("enter search item: "))
for item in dict1:
    if item==search:
        print("Item found!")
        break
else:
    print("Item not found")