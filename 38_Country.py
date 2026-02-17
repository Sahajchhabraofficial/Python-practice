#Write a program using switch-case that takes the first letter of a country name as input and prints a full country name starting with that letter.
country=input("Enter contry's short form: ")
match country:
    case 'PAK': print("Gareeb Desh (Pakistan)")
    case 'IND': print("Mera bharat mahan (India)")
    case 'US': print("Kuch keh nahi sakta(America)")
    case 'UK': print("Angrejo ka Desh (Britain)")
    case 'RUS': print("Sabse bada desh(Russia)")
    case _: print("Man nahi hai batane ka!")