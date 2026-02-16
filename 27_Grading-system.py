#Determine the grade based on marks. 
# Marks (90-100) A grade 
# Marks (75-89) B grade 
# Marks (50-74) C grade 
# Marks ( < 50) F grade
percentage=int(input("Enter your percentage: "))
if percentage<=100 and percentage>=90:
    print("A Grade")
elif percentage<=75 and percentage>=89:
    print("B Grade")
elif percentage<=50 and percentage>=74:
    print("C Grade")
elif percentage<50:
    print("F Grade")
else:
    print("Fail")
