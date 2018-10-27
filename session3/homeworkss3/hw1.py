print("hi there,this is a supper user gate way")
usname=input("User name: ")
if usname != "c4e":
    print("u are not a superuser")
else:
    pas=input("Password: ")
    if pas != "codethechange":
        print("password incorrect")
    else:
        print("welcome, ",usname)

