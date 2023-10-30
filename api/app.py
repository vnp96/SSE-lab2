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


# @app.route("/query", methods=["GET"])
# def get_query():
#    return render_template("url_hacking.html",
#                           ans_string=process_query(request.args.get("q")))

@app.route("/query", methods=["GET"])
def process_query():
    query_param = request.args.get("q")
    if "dinosaurs" in query_param:
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif "asteroids" in query_param:
        return "Unknown"
    else:
        return "You cheeky bugger, you gotta try everything don't you?"
