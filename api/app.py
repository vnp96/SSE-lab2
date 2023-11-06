from flask import Flask, render_template, request
import requests
import json

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


@app.route("/git_info", methods=["POST"])
def render_git_page():
    git_username = request.form.get("git_username")

    url = "https://api.github.com/users/{YOUR_GITHUB_USERNAME}/repos"
    url = url.replace("{YOUR_GITHUB_USERNAME}", git_username)

    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()  # data returned is a list of ‘repository’ entities
        return render_template("repositories.html",
                               git_user=git_username,
                               repositories=repos,
                               # ans_string=json.dumps(repos, indent=4)
                               )
    else:
        return process_query(git_username)


@app.route("/query", methods=["GET"])
def get_query():
    return process_query(request.args.get("q"))


def get_numbers(input_String):
    numbers = input_String.strip('?').split(':')[1].split(',')
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i].strip())
    return numbers


def get_plus_query_ans(query_param):
    args = query_param.strip('?').split()
    nums = []
    for arg in args:
        if arg.isnumeric():
            nums.append(int(arg))

    return sum(nums)


def getSquareCubes(lst):
    for x in lst:
        cube = int(round(x ** (1. / 3))) ** 3 == x
        square = int(round(x ** (1. / 2))) ** 2 == x
        if cube and square:
            return x


def get_mul_query_ans(query_param):
    args = query_param.strip('?').split()
    prod = 1
    for arg in args:
        if arg.isnumeric():
            prod *= int(arg)

    return prod


def process_query(query_param):
    query_param = query_param.lower()
    if "largest" in query_param and "numbers" in query_param:
        return str(max(get_numbers(query_param)))
    elif "plus" in query_param:
        return str(get_plus_query_ans(query_param))
    elif "multiplied" in query_param:
        return str(get_mul_query_ans(query_param))
    elif "square" in query_param and "cube" in query_param:
        return str(getSquareCubes(get_numbers(query_param)))
    elif "dinosaurs" in query_param:
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif "asteroids" in query_param:
        return "Unknown"
    elif "what is your name" in query_param:
        return "Vishnu"
    else:
        return "You cheeky bugger, you gotta try everything don't you?"
