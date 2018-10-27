items=["T-shirt","Sweater"]
stment=input("Welcome to our shop,what do you want (C,R,U,D)?")
while True:
    if stment=="C" or stment=="c":
        new_items=input("enter new item:")
        items.append(new_items)
        print("our items: ",end='')
        print(*items,sep=", ")
        stment=input("what do you want more (C,R,U,D)?")
    elif stment=="R" or stment=="r":
        print("our items: ",end='')
        print(*items,sep=", ")
        stment=input("what do you want more (C,R,U,D)?")
    elif stment=="U" or stment=="u":
        position=int( input("position to change?"))
        while position > len(items):
            print("index out of range")
            position=int( input("position to change?"))
        new_items=input("new item?")
        items[position-1]=new_items
        print("our items: ",end='')
        print(*items,sep=", ")
        stment=input("what do you want more (C,R,U,D)?")
    elif stment=="D" or stment=="d":
        position=int( input("position to delele?"))
        while position > len(items):
            print("index out of range")
            position=int( input("position to delete?"))
        items.pop(position-1)
        print("our items: ",end='')
        print(*items,sep=", ")
        stment=input("what do you want more (C,R,U,D)?")
    else:
        print("wrong syntax")
        stment=input("what do you want (C,R,U,D)?")

    



