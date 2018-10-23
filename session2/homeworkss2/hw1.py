h=int(input("height?(cm)"))
w=int(input("WEIGHT?(kg)"))
bmi= w/((h/100)**2)
print(bmi)
if bmi<16:
    print("u are severely underweight")
elif bmi<18.5:
    print("u are underweight")
elif bmi<25:
    print("u are normal")
elif bmi<30:
    print("u are overweight")
else:
    print("u are obese")
    
    
