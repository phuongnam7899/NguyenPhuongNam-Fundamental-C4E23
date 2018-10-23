a= int(input("nhap a"))
b= int(input("nhap b"))
c= int(input("nhap c"))
delta= b*b - 4*a*c
if delta < 0:
    print("pt vo nghiem")
elif delta == 0:
    x=-b/(2*a)
    print("pt co nghiem kep:",x)
else:
    x1= (-b+(delta**(1/2)))/(2*a)
    x2= (-b-(delta**(1/2)))/(2*a)
    print("pt co 2 nghiem phan biet: x1=",x1,"va x2=",x2)