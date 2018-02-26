from flask import Flask, render_template
app = Flask(__name__)


@app.route('/BMI/<int:weight>/<int:height>')
def BMI(weight,height):
    height = height * 0.01
    bmi = weight / (height ** 2)

    if bmi < 16:
        result = "Severely underweight"
    elif bmi < 18.5:
        result = "Underweight"
    elif bmi < 25:
        result = "Normal"
    elif bmi < 30:
        result = "Overweight"
    else:
        result = "Obese"

    Input_bmi = {
        "Weight" : str(weight),
        "Height" : str(height),
        "BMI": str(bmi),
        "Result" : str(result)
    }
    return render_template('BMI.html', bmi = Input_bmi )

if __name__ == '__main__':
  app.run(debug=True)
