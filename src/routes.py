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

@app.route("/deletetip/<id>")
def delete_tip(id):
    if readingtip_service.delete_tip(id):
        return redirect("/")
    else:
        flash("Delete failed")
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
