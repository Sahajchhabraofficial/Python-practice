#Write a program to calculate the total salary based on the basic salary:
# If BS in between 4000-6000  ta 40% & hra is 20%
# If BS in between 6000-10000  ta 45% & hra is 20%
# If BS is greater than 10000  ta 55% & hra is 5000
Basicsallary=int(input("enter basic sallary: "))

if Basicsallary >= 4000 and Basicsallary <= 6000:
    ta = Basicsallary * 0.40
    hra = Basicsallary * 0.20
elif Basicsallary > 6000 and Basicsallary <= 10000:
    ta = Basicsallary * 0.45
    hra = Basicsallary * 0.20
elif Basicsallary > 10000:
    ta = Basicsallary * 0.55
    hra = 5000
else:
    print("Basic salary should be at least 4000")
    exit()

total_salary = Basicsallary + ta + hra

print(f"Basic Salary: {Basicsallary}")
print(f"TA: {ta}")
print(f"HRA: {hra}")
print(f"Total Salary: {total_salary}")