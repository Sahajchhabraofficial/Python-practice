#Write a program using switch-case to print your friend's name based on the first letter of their name.
short=input("Enter a nickname: ")
short.upper()   
match short:
    case "S": print("Your friends name is: Sahaj Chhabra")
    case "B": print("Your Friend's name is: Bhubali")
    case "T": print("Your friend's name is: Tony Stark")
    case "R": print("Your friend's name is Rehmaan Dakait") 
    case _:
        print("Your friend is dead!!")