#items = [] #empty list
#print(items)
#print(type(items))
#C: creat; R:read;U:update;D:delete(CRUD)

items=["g","sh"] 
i= int(input("index?"))
new_value=input("new value")
items[i]= new_value
print(new_value)
#print(items[1])
#coi moi ptu la 1 bien

items.pop(1)# xoa theo index
items.remove("g")#xoa theo gia tri



