pw=input("nhap pass")
while True:
    if  pw.isupper() or  pw.islower() or pw.isdigit() :
        print("phai co ca chu hoa va thuong")
    elif pw.isalpha() :
        print("phai chua so")
    elif not len(pw)>8:
        print("phai chua tren 8 ki tu")
    else:
        break
    pw=input("nhap pass")
print("Your password is OK")