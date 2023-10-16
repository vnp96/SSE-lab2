from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")
    # return "Hello I am alive!!"


@app.route("/age_calculator", methods=["POST"])
def submit():
    curr_age = int(request.form.get("curr_age"))
    year_now = int(request.form.get("year_now"))
    target_year = int(request.form.get("target_year"))

    # logic for age at target year
    target_age = target_year - (year_now - curr_age)
    return render_template("age_calculator_result.html",
                           target_year=target_year,
                           target_age=target_age)
