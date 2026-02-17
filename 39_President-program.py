#Write a program using switch-case (or if-else if using strings) to take the first letter of a country name as input, and print the President's name based on that.
country=input("Enter first letter of the country: ")
match country:
    case "I":
        print("Draupadi murmu")
    case "P":
        print(" Asif Ali Zardari. ")
    case "A":
        print("Donald Trump")
    case "B":
        print("Keir Starmer")
    case _:
        print("Chalo bye...")