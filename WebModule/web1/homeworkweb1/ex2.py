from flask import Flask,render_template

app = Flask(__name__)

@app.route("/user/<username>")
def user_info(username):
    users = [
        {
            "name": "nam" ,
            "full name": "Nguyễn Phương Nam" ,
            "gender":"Male" ,
            "age": 19,
            "hobby": "Coding"
        },
        {
            "name":"huy",
            "full name":"Nguyễn Quang Huy",
            "gender":"Male",
            "age":29,
            "hobby":"Sleep"
        },
        {
            "name":"quan",
            "full name":"Nguyễn Anh Quân",
            "gender":"Male",
            "age":22,
            "hobby":"Pha trà, cắm hoa"
        },
        {
            "name":"duc",
            "full name":"(Nguyễn) Hoàng Đức",
            "gender":"Male",
            "age":22,
            "hobby":"Thỉnh kinh"
        }
    ]
    name_list=[]
    att_list = ["full name","gender","age","hobby"]
    info_list = []
    new_list=[]
    count = 0
    for user in users:
        if username == user["name"]:
            count += 1
            choose_user = user
            for att in att_list:
                info_list.append(choose_user[att])
            for i in range(4):
                s= str(att_list[i]) + " : " + str(info_list[i])
                new_list.append(s)
            return render_template("user.html",user_list= new_list)
    if count == 0:
        return "user not found"
        
   

if __name__ == "__main__":
    app.run(debug=True)