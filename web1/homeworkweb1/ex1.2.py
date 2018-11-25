from flask import Flask,render_template

app = Flask(__name__)

@app.route ("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    bmi_calc = weight/(height*height/10000)
    if bmi_calc < 16:
        condi = "severely underweight"
    elif bmi_calc < 18.5:
        condi = "underweight"
    elif bmi_calc < 25:
        condi = "normal"
    elif bmi_calc < 30:
        condi="overweight"
    else:
        condi="obese"
    return render_template("bmi.html",bmi = bmi_calc, condition = condi )

if __name__ == "__main__":
    app.run(debug= True)