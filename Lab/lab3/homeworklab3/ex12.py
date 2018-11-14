from ex12357911 import is_insight
boolean = False
count=0
for x in range(141,240):
    for y in range (61,260):
        if is_insight([x,y],[140,60,100,200]) == False:
            count += 1
if count == 0:
    print("your code are true")
else:
    print("your codes are wrong")

