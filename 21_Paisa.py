#Write a program to display two massage first is press 1 for converts amount into (500,50,10,1 notes) and Press 2 for converts amount into (200,100,20,5,2 notes) and display result
amount=int(input("Enter amount: "))
press=int(input("Pass a key (1 or 2):"))
if press==1:
    five_hundred=amount//500
    amount=amount%500
    fifty=amount//50
    amount=amount%50
    ten=amount//10
    amount=amount%10
    print("Five hundred: ",five_hundred)
    print("Fifty: ",fifty)
    print("Ten: ",ten)
    print("One: ",amount)
elif press==2:
    two_hundred=amount//200
    amount=amount%200
    hundred=amount//100
    amount=amount%100
    twenty=amount//20
    five=amount//20
    two=amount//2
    amount=amount%2
    print("two hundred: ",two_hundred)
    print("hundred: ",hundred)
    print("twenty: ",twenty)
    print("two: ",two)
    print("five: ",five)
else:
    print("Invalid key passed!")