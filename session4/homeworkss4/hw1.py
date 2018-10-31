size_list=[69,96,669,996,696,969]
print("my name is Nam and these are my sheep sizes")
print(size_list)
#-----------------------------------------------------------------
size_max = size_list[1]
for i in size_list:
    if i > size_max:
        size_max = i
print("now my biggest sheep has size",size_max,",let's shear it!")
#-----------------------------------------------------------------
for i in range(len(size_list)):
    if size_list[i]== size_max:
        size_list[i] = 8
print("after shearing,here is my flock:")
print(size_list)
#------------------------------------------------------------------
for i in range(len(size_list)):
        size_list[i] += 50
print("1 month passed,now here is my flock:")
print(size_list)
#------------------------------------------------------------------
for month in range(1,21):
        print("Month",month)
        for i in range(len(size_list)):
                size_list[i] += 50
        print("1 month passed,now here is my flock:")
        print(size_list)

        size_max = size_list[1]
        for i in size_list:
                if i > size_max:
                        size_max = i
        print("now my biggest sheep has size",size_max,",let's shear it!")
        
        for i in range(len(size_list)):
                if size_list[i]== size_max:
                        size_list[i] = 8
        print("after shearing,here is my flock:")
        print(size_list)
#--------------------------------------------------------------------
print("Month 21")
for i in range(len(size_list)):
        size_list[i] += 50
print("1 month passed,now here is my flock:")
print(size_list)
sum_size=0
for i in size_list:
        sum_size += i
print("my flock has size in total:",sum_size)
print("i would get: ",sum_size,"* 2$ = ",sum_size*2,"$")
        
