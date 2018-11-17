from flask import Flask, render_template

app = Flask(__name__)


# functin binding
@app.route("/") # if user go to home,run this function
def home():
    return "hello" # tranform to html and send to browser

@app.route("/c4e")
def c4e():
    return "hello c4e,hih"

@app.route("/me")
def me():
    return "nam"

 
@app.route("/hi/<name>")
def hi_name(name):
    return "hi " + name

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    s= str(a +b)
    return s
    return a # must be a string


@app.route("/posts/<int:index>")
def posts(index):
    titles = ["1","2","3","4"]
    contents=["1","2","3","4"]
    return render_template("post.html", title = titles[index-1],content = contents[index-1])

@app.route("/movie")
def movie():
    return render_template("onermovie.html", name = "deadpool", image = "https://i.ebayimg.com/images/g/jzkAAOSwVoFaqV-L/s-l300.jpg")

@app.route("/movies")
def movies():
    # movie_title = [
    #     "deadpool",
    #     "bw",
    #     "cap",
    #     "iron"
    # ]
    movie_list=[
        {
            "title":"a",
            "image":"https://i.ebayimg.com/images/g/jzkAAOSwVoFaqV-L/s-l300.jpg",
        },
        {
            "title":"b",
            "image":"https://i.ebayimg.com/images/g/jzkAAOSwVoFaqV-L/s-l300.jpg",
        },
        {
            "title":"c",
            "image":"https://i.ebayimg.com/images/g/jzkAAOSwVoFaqV-L/s-l300.jpg",
        }
    ]
    return render_template("movies.html", movies = movie_list )
if __name__ == "__main__":
    app.run( debug= True )
