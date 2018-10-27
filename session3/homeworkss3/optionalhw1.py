from random import *
secret_num= randint(1,101)
guess_num= int(input("guess my number:"))
while guess_num>100 or guess_num<1:
    print("1-100 only")
    guess_num= int(input("guess my number:"))
while not guess_num==secret_num:
    if guess_num>secret_num:
        print("too high")
        guess_num= int(input("guess my number:"))
    else:
        print("too low")
        guess_num= int(input("guess my number:"))
print("bingo!!!")
