solama={
    1:"I",
    2:"II",
    3:"III",
    4:"IV",
    5:"V",
    6:"VI",
    7:"VII",
    8:"VIII",
    9:"IX",
    10:"X",
}
print("day la tu dien so he thap phan - so la ma (pham vi tu 1-10)")


while True:
    so = int(input("nhap chu so can chuyen doi sang so la ma(1-10):"))
    if so not in solama:
        boole=input("key not found,do you want to add?").upper()
        if (boole=="Y"):
            mean=input("nhap so la ma tuong ung")
            solama[so]=mean
    else:
        print(solama[so])
    
