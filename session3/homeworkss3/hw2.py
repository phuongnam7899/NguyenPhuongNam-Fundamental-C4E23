print("hi there,this is a supper user gate way")
usname=input("User name: ")
while usname != "c4e":
    print("u are not a superuser")
    usname=input("User name: ")
pas=input("Password: ")
while pas != "codethechange":
        print("password incorrect")
        pas=input("Password: ")
print("welcome, ",usname)