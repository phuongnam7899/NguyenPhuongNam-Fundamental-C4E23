from flask import Flask,render_template,request
import mlab
from register import Register
from gmail import GMail,Message

mlab.connect()

app = Flask(__name__)


@app.route("/registerr", methods=["GET","POST"])
def registerr():
    # gửi cho ng dùng form điền để lấy thông tin 
    if request.method == "GET":
        return render_template("register.html")
    # lưu thông tin ng dùng gửi vào dtb
    elif request.method == "POST":
        # form sẽ chứa usn,pw,mail
        form = request.form
        usn = form["usn"]
        pw = form["pw"]
        m = form["mail"]

        exist = Register.objects(user_name=usn).first()
        # nếu ng dùng chưa tồn tại thì mới lưu
        if exist != None:
            return "ussername already existed"
        else:
            r = Register(user_name=usn,pass_word=pw,mail=m)
            r.save()
            gmail= GMail("nguyenphuongnam7899@gmail.com","namyeuthanh2503")
            message = Message("Welcome",to=m,html="<p>heloo</p>")
            gmail.send(message)
            return "We have sent an e-mail for you"


if __name__ == "__main__":
    app.run()