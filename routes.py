from app import app
from flask import render_template, request, redirect, session, abort
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
    a = messages.get_desc(id)[0]

    user_id = users.user_id()
    list = messages.get_list_for_menu(user_id)
    isCourses = True
    if list:
        if len(list) > 0:
            isCourses = False
    

    if material == None:
        return render_template("error.html", message="materiaalia ei löytynyt")
    else:
        return render_template("coursetemplate.html", material=a, desc=material[1], isCourses=isCourses,course=id)
    
@app.route("/kurssi/<int:id>/<int:id2>")
def page2(id, id2):
    a = messages.search_content(id,id2)
    b = messages.search_polls(id,id2)
    print(b)
    return render_template("coursepage.html", id2 = a, seuraava = id2 + 1, seuraava2 = id, choices = b[1], topic=b[0])
    
    

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
        
        course = messages.get_course(id)
        user_id = users.user_id()
        a = messages.get_user_from_course(id)


        if "add_course" in request.form and request.form["add_course"] == "add":
            if session["csrf_token"] != request.form["csrf_token"] or user_id != a[0]:
                abort(403)
            else:
                topic = request.form["topic"]
                pagenum = request.form["pagenumber"]
                sql = "INSERT INTO polls (topic, created_at, course_id,pagenumber) VALUES (:topic, NOW(), :id,:pagenumber) RETURNING id"
                result = db.session.execute(text(sql), {"topic":topic, "id":id, "pagenumber":pagenum})
                poll_id = result.fetchone()[0]
                choices = request.form.getlist("choice")
                for choice in choices:
                    if choice != "":
                        sql = "INSERT INTO choices (poll_id, choice) VALUES (:poll_id, :choice)"
                        db.session.execute(text(sql), {"poll_id":poll_id, "choice":choice})
                db.session.commit()
                return redirect("/")


        elif "action" in request.form and request.form["action"] == "delete":
            if session["csrf_token"] != request.form["csrf_token"] or user_id != a[0]:
                abort(403)
            else: 
                messages.delete_course(id)
                return redirect("/menu")
            
        elif "add_text" in request.form and request.form["add_text"] == "add2":
            if session["csrf_token"] != request.form["csrf_token"] or user_id != a[0]:
                abort(403)
            else: 
                thetext = request.form["textforcourse"]
                pagenum2 = request.form["pagenumber2"]
                sql = "INSERT INTO coursecontent (course_id, textcontent, pagenumber) VALUES (:id, :text, :page)"
                result = db.session.execute(text(sql), {"id":id, "text":thetext, "page":pagenum2})
                db.session.commit()
                return redirect(f"/edit/{id}")



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