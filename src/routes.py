from flask import redirect, render_template, request, flash
from app import app
from services.readingtip_service import readingtip_service
from services.user_service import user_service
from services.tag_service import tag_service

@app.route("/newtip", methods=["POST"])
def newtip():
    title = request.form["title"]
    tags =  request.form["tags"].split(",")
    strippedTags = [tag.strip() for tag in tags if tag.strip() != ""]
    if readingtip_service.contains_title(title):
        flash(f"Tips already contains tip with title {title}")
        return redirect("/newtip")
    readingtip_service.create_tip(title, request.form["link"], strippedTags)
    return redirect("/")

@app.route("/newtip")
def create_tip():
    return render_template("newtip.html")

@app.route("/changetip/<id>", methods=["GET","POST"])
def change_tip(id):
    if request.method == "POST":
        edited_title = request.form["edited_title"]
        edited_link = request.form["edited_link"]
        tags = request.form["edited_tags"].split(",")
        strippedTags = [tag.strip() for tag in tags if tag.strip() != ""]

        tip = readingtip_service.get_tip(id)

        if readingtip_service.contains_title(edited_title) and edited_title != tip.title:
            flash(f"Tips already contains tip with title {edited_title}")
            return redirect("/")

        if not edited_title or not edited_link:
            flash(f"Tip editing failed: title or link cannot be empty")
            return redirect("/")

        if readingtip_service.change_tip(tip, edited_title, edited_link, strippedTags):
            flash("Tip edited successfully")
            return redirect("/")
        else:
            flash("Tip editing failed")
            return redirect("/")

    if request.method == "GET":
        tip = readingtip_service.get_tip(id)
        tags = ", ".join(readingtip_service.get_tag_names(tip))
        return render_template("changetip.html", tip=tip, tags=tags)

@app.route("/deletetip/<id>")
def delete_tip(id):
    if readingtip_service.delete_tip(id):
        return redirect("/")
    else:
        flash("Delete failed")
        return redirect("/")

@app.route("/readtip/<id>")
def read_tip(id):
    if readingtip_service.read_tip(id):
        return redirect("/")
    else:
        flash("Marking tip as read failed")
        return redirect("/")

@app.route("/")
def userpage():
    if user_service.is_authenticated():
       tips=readingtip_service.get_tips()
       tags =tag_service.get_tags()
       return render_template("userpage.html", tips=tips, tags=tags)
    else:
        return render_template("login.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user_service.login(username, password):
            flash("Login successful")
            return redirect("/")
        else:
            flash("Login failed")
            return redirect("/")
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    user_service.logout()
    return redirect("/")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user_service.register(username, password):
            flash("Registration successful, you are now logged in")
            return redirect("/")
        else:
            flash("Register failed")
            return redirect("/")
    else:
        return render_template("register.html")

@app.route("/ping")
def ping():
    return "ping"
