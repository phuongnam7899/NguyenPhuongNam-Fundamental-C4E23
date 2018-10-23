print("bai 4a")
for i in range(20):         
    print("* ", end ='')
print()

print("bai 4b")
m=int(input("enter m:"))
for i in range(m):
    print("* ", end='')
print()

print("bai 4c")
print("x",end='')
for i in range(4):
    print(" * x", end='')
print()

print("bai 4d")
n=int(input("nhap n:"))
for i in range(n):
    if i%2==0:
        print("x ",end='')
    else:
        print("* ",end='')
print()

print("bai 4e")
print()

print("bai 4f")
for i in range(3):
    for k in range(7):
        print("* ",end='')
    print()
print()

print("bai 4g")
n=int(input("nhap so cot n"))
m=int(input("nhap so hang m"))
for i in range(m):
    for k in range(n):
        print("*  ",end='')
    print()
print()
