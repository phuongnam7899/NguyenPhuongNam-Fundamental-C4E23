from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route("/about-me")
def about_me():
    info_list =[
        {
            "title":"Name",
            "image":"https://steamcdn-a.akamaihd.net/steam/apps/329650/header.jpg?t=1468248576"
        },
        {
            "title":"Date of birth",
            "image":"http://etc.usf.edu/clipart/37200/37213/frac_07-08_37213_lg.gif"
        },
        {
            "title":"Work",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWE4jK_ySoTrNSYHePEnEIoUGgEyIYbGnJI2bJZdYUVPvgnB9g3w"
        },
        {
            "title":"School",
            "image":"https://sie.hust.edu.vn/wp-content/uploads/2016/04/sie.hust.edu.vn-19.jpg"
        },
        {
            "title":"Hobby",
            "image":"https://cdn-images-1.medium.com/max/1600/1*iFN_PWPWs6TQ9JzDp2v9Wg.jpeg"
        },
        {
            "title":"crush",
            "image":"https://scontent.fhan1-1.fna.fbcdn.net/v/t1.0-9/13718620_922226527924157_5532120584519015466_n.jpg?_nc_cat=111&_nc_ht=scontent.fhan1-1.fna&oh=141b449ea37ee4bdfd218b139e3aed55&oe=5C7DFEE9"
        },
    ]
    return render_template("about_me.html", infos = info_list)

@app.route("/school")
def school():
    return redirect("http://techkids.vn", code= 302,Response= None)


if __name__ == "__main__":
    app.run(debug=True)