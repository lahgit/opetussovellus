from app import app
from flask import render_template, request, redirect
import messages, users

from db import db
from sqlalchemy.sql import text

@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", count=len(list), messages=list)

@app.route("/kurssi/<int:id>")
def page(id):
    material = messages.read_course_material(id)
    return render_template("coursetemplate.html", material=material)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/menu")
def menu():
    user_id = users.user_id()
    list = messages.get_list_for_menu(user_id)
    return render_template("coursemanagermenu.html", messages=list)

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    description = request.form["description"]
    textcontent = request.form["contentforcourse"]
    if messages.send(content,description,textcontent):
        return redirect("/")
    else:
        return render_template("error.html", message="Kurssin lisäys ei onnistunut")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")