#Write a program to input electricity unit and calculate total electricity bill according to the given condition: 
# For first 50 units Rs. 0.50/unit 
# For next 100 units Rs. 0.75/unit 
# For next 100 units Rs. 1.20/unit 
# For unit above 250 Rs. 1.50/unit 
# An additional surcharge of 20% is added to the bill
Units=int(input("Enter total units: "))
bill = 0
if Units <= 50:
    bill = Units * 0.50
elif Units <= 150:
    bill = (50 * 0.50) + ((Units - 50) * 0.75)
elif Units <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + ((Units - 150) * 1.20)
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((Units - 250) * 1.50)
# Add 20% surcharge
surcharge = bill * 0.20
total_bill = bill + surcharge
print(f"Units Consumed: {Units}")
print(f"Bill Amount: Rs. {bill}")
print(f"Surcharge (20%): Rs. {surcharge}")
print(f"Total Bill: Rs. {total_bill}")
