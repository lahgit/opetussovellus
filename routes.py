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

    user_id = users.user_id()
    list = messages.get_list_for_menu(user_id)
    isCourses = True
    if list:
        if len(list) > 0:
            isCourses = False
    

    if material == None:
        return render_template("error.html", message="materiaalia ei löytynyt")
    else:
        return render_template("coursetemplate.html", material=material[0], desc=material[1], isCourses=isCourses)
    

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        course = messages.get_course(id)
        user_id = users.user_id()
        a = messages.get_user_from_course(id)
        material = messages.read_course_material(id)

        if material == None:
            return render_template("error.html", message="materiaalia ei löytynyt")

        if user_id == a[0]:
            return render_template("editmenu.html",info=course[0])
        else: return render_template("error.html", message="ei oikeutta muokata kurssia")
    if request.method == "POST":
        if request.form["action"] == "delete":
            messages.delete_course(id)

            return redirect("/menu")



@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/menu")
def menu():
    user_id = users.user_id()
    list = messages.get_list_for_menu(user_id)
    isCourses = False
    if list:
        if len(list) > 0:
            isCourses = True

    return render_template("coursemanagermenu.html", messages=list, isCourses=isCourses)



@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    description = request.form["description"]
    textcontent = request.form["contentforcourse"]
    if messages.send(content,description,textcontent):
        return redirect("/")
    else:
        return render_template("error.html", message="Kurssin lisäys ei onnistunut")
    
@app.route("/courses")
def kurssilista():
    list = messages.get_list()
    return render_template("courselist.html", messages=list)

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