from gmail import GMail,Message
from datetime import *
gmail= GMail("nguyenphuongnam7899@gmail.com","namyeuthanh2503")
while True:
    if datetime.now().hour == 7 :
        message= Message("hello, ",to="qhuydtvt@gmail.com",text="em xin nghi a")
        gmail.send(message)
        break
print("sent")