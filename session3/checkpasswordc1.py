pw=input("nhap pass")
while  pw.isupper() or  pw.islower() or pw.isdigit() or  (not len(pw)>8):
    if  pw.isupper() or  pw.islower() or pw.isdigit() :
        print("phai co ca chu hoa va thuong")
    if pw.isalpha() :
        print("phai chua so")
    if not len(pw)>8:
        print("phai chua tren 8 ki tu")
    pw=input("enter password:")
print("Your password is OK")