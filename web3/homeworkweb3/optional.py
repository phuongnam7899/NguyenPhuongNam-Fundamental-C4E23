import mlab
from to_do_list import To_do_list

mlab.connect()

def new_to_do():
    name = input("Enter your new to-do: ")
    description = input("Add more description: ")
    completed = "No"
    new_todo = To_do_list(name= name,description=description,completed=completed)
    new_todo.save()
    print("Saved")
def view_all():
    to_dos = To_do_list.objects()
    i = 1
    listt = []
    for to_do in to_dos:
        listt.append(to_do.name)
    if listt == [] :
        print("EMPTY")
    for to_do in to_dos:

        print(i,".",sep="")
        print("Name:",to_do.name)
        print("Description:",to_do.description)
        print("Completed:",to_do.completed)
        i += 1

def mark_completed():
    index = int(input("Which one you COMPLETED? "))
    to_dos = To_do_list.objects()
    i = 1
    for to_do in to_dos:
        if i == index:
            to_do.completed = "Yes"
            to_do.save()
            pass
        i += 1
    print("Changed")
        

def delete_todo():
    index = int(input("Which one you want to DELETE? "))
    to_dos = To_do_list.objects()
    i =1
    for to_do in to_dos:
        if index == i :
            to_do.delete()
            pass
        i += 1
    print("Deleted")
        

commands = ["New to-do","View ALL to-do","Mark a to-do COMPLETED","Delete a to-do","Exit"]
for i,cm in enumerate(commands):
    print( i+1, cm)

while True:
    command = int(input("Enter your command? "))
    if command not in range(1,6):
        print("Syntax Error")
    else:
        if command == 1:
            new_to_do()
        elif command == 2:
            view_all()
        elif command == 3:
            mark_completed()
        elif command == 4:
            delete_todo()
        else:
            print("bye")
            break

        










