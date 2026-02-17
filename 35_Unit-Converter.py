#Write a program to make simple converter. 
# Press 1 to convert weight Kg to gram 
# Press 2 to convert distance meter to c.m 
# Press 3 to convert indian currency into doller 
# Press 4 to convert temperature Celsius to Fahrenheit.
print("=====WELCOME TO MY UNIT CONVERTER=====")
print("Press 1 to convert weight Kg to gram")
print("Press 2 to convert distance meter to c.m ")
print("Press 3 to convert indian currency into doller")
print("Press 4 to convert temperature Celsius to Fahrenheit")
choice=int(input("Enter your choice: "))
match choice:
    case 1:
        Kg=int(input("Enter weight in Kgs:"))
        print(f"Weight in grams: {Kg*1000}")
    case 2:
        meter=int(input("Enter distance in meters: "))
        print(f"Distance in centimeters: {meter*100}")
    case 3:
        indian=int(input("Enter currency in indian rupees: "))
        print(f"Currency in USD: {indian*0.011}")
    case 4:
        celcius=int(input("Enter temprature in celsius: "))
        print(f"Temprature in Fahrenheit: {((9/5)*celcius)+32}")
    case _:
        print("This conversion isn't available!")