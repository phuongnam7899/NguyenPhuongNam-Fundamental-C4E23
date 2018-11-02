string = input("enter string: ").lower()
str_list =list(string)
str_list.sort()
k=[]
for i in str_list:
     while True:
        if i in k:
             break
        else:
            if i == " ":
                break
            else:
                print(i, str_list.count(i), sep=": ")
                k.append(i)
                break