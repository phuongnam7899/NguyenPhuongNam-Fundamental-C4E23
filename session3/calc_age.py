yob_str= input("year of birth?")
while not yob_str.isdigit():
    print("all digit please!")
    yob_str= input("year of birth?")

yob=int(yob_str)
age=2018-yob
print("your age is: ",age)