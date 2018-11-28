from flask import Flask,render_template,request
import mlab
from bike import Bike

mlab.connect()
app = Flask(__name__)

@app.route("/new_bike",methods=["POST","GET"])
def new_bike():
    if request.method == "GET":
        return render_template("bike_rent.html")
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        fee = form["fee"]
        img = form["image"]
        year = form["year"]
        new = Bike(model=model,daily_fee=fee,image=img,year=year)
        new.save()
        return "saved"

if __name__ == "__main__":
    app.run(debug=True)