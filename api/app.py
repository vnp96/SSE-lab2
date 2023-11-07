from datetime import datetime

import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def homepage():
    chuck_joke = ""
    dad_joke = ""
    chucky = requests.get("https://api.chucknorris.io/jokes/random")
    if chucky.status_code == 200:
        chuck_joke = chucky.json()["value"]

    api_ninja_key = "82DDzW+fT044IK+VgjL1nw==uRsEaKdOUBT9WHSp"
    dad_joke_response = requests.get("https://api.api-ninjas.com/v1/dadjokes"
                                     "?limit={}".format(1),
                                     headers={"X-Api-Key": api_ninja_key})
    if dad_joke_response.status_code == 200:
        dad_joke = dad_joke_response.json()[0]["joke"]

    return render_template("index.html",
                           chuck_joke=chuck_joke,
                           dad_joke=dad_joke)


@app.route("/age_calculator", methods=["POST"])
def age_calculator_page():
    curr_age = int(request.form.get("curr_age"))
    year_now = int(request.form.get("year_now"))
    target_year = int(request.form.get("target_year"))

    # logic for age at target year
    target_age = target_year - (year_now - curr_age)
    return render_template("age_calculator_result.html",
                           target_year=target_year,
                           target_age=target_age)


@app.route("/git_lookup", methods=["POST"])
def git_lookup():
    git_username = request.form.get("git_username")

    url = "https://api.github.com/users/{YOUR_GITHUB_USERNAME}/repos"
    url = url.replace("{YOUR_GITHUB_USERNAME}", git_username)

    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        google_github_search = ("https://www.google.com/search?q={"
                                "author_name}+github")

        stripped_repos = []
        for repo in repos:
            stripped_repo_data = {}
            stripped_repo_data["name"] = repo["name"]
            date_time = datetime.strptime(repo["updated_at"], '%Y-%m-%dT%H:%M'
                                                              ':%SZ')
            stripped_repo_data["last_updated"] = date_time.strftime('%Y-%m-%d '
                                                                    '%H:%M:%S')

            latest_commit_response = requests.get(
                repo["commits_url"].replace("{/sha}", ""))
            latest_commit_info = {}
            if latest_commit_response.status_code == 200:
                latest_commit_data = latest_commit_response.json()[0]

                latest_commit_info["hash"] = latest_commit_data["sha"]
                latest_commit_info["html_url"] = latest_commit_data["html_url"]
                latest_commit_info["author"] = \
                    latest_commit_data["commit"]["author"]["name"]
                latest_commit_info[
                    "author_url"] = google_github_search.replace(
                    "{author_name}",
                    latest_commit_info["author"].replace(" ", "+"))
                latest_commit_info["commit_message"] = \
                    latest_commit_data["commit"]["message"]

            else:
                latest_commit_info["hash"] = ""
                latest_commit_info["html_url"] = ""
                latest_commit_info["author_url"] = ""
                latest_commit_info["author"] = ""
                latest_commit_info["commit_message"] = ""

            stripped_repo_data["latest_commit"] = latest_commit_info
            stripped_repos.append(stripped_repo_data)

        return render_template("repositories.html",
                               git_user=git_username,
                               repositories=stripped_repos)
    else:
        return process_query(git_username)


@app.route("/query", methods=["GET"])
def page_less_query():
    return process_query(request.args.get("q"))


@app.route("/jokes", methods=["GET"])
def jokes_page():
    return "Insert jokes"


def get_numbers(input_string):
    numbers = input_string.strip('?').split(':')[1].split(',')
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


def get_square_cubes(lst):
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
        return str(get_square_cubes(get_numbers(query_param)))
    elif "dinosaurs" in query_param:
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif "asteroids" in query_param:
        return "Unknown"
    elif "what is your name" in query_param:
        return "Vishnu"
    else:
        return "You cheeky bugger, you gotta try everything don't you?"
