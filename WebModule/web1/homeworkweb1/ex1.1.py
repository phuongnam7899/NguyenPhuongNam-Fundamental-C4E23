from flask import Flask

app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    bmi_calc = weight/(height*height/10000)
    if bmi_calc < 16:
        return str(bmi_calc) + " :severely underweight "
    elif bmi_calc < 18.5:
        return str(bmi_calc) + " :underweight"
    elif bmi_calc < 25:
        return str(bmi_calc) + " :normal"
    elif bmi_calc < 30:
        return  str(bmi_calc) + " :overweight"
    else:
        return str(bmi_calc) + " :obese "
if __name__ == "__main__":
    app.run(debug= True)