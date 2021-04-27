from flask import redirect, render_template, request, flash
from app import app
from services.readingtip_service import readingtip_service
from services.user_service import user_service
from services.tag_service import tag_service

def flash_error(error):
    error = error.args[0] if len(error.args) > 0 else None
    category = "warning"
    if error is None:
        error = "Not authorized"
        category = "danger"
    flash(error, category)

@app.route("/newtip", methods=["POST"])
def newtip():
    title = request.form["title"]
    link = request.form["link"]
    tags = request.form["tags"].split(",")
    strippedTags = [tag.strip() for tag in tags if tag.strip() != ""]
    try:
        readingtip_service.create_tip(title, link, strippedTags)
    except AssertionError as error:
        flash_error(error)
        return redirect("/newtip")
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

        try:
            readingtip_service.change_tip(tip, edited_title, edited_link, strippedTags)
            flash("Tip edited successfully", "success")
            return redirect("/")
        except AssertionError as error:
            flash_error(error)
            return redirect("")

    if request.method == "GET":
        tip = readingtip_service.get_tip(id)
        tags = ", ".join(readingtip_service.get_tag_names(tip))
        return render_template("changetip.html", tip=tip, tags=tags)

@app.route("/deletetip/<id>")
def delete_tip(id):
    try:
        readingtip_service.delete_tip(id)
        return redirect("/")
    except AssertionError as error:
        flash_error(error)
        return redirect("/")

@app.route("/readtip/<id>")
def read_tip(id):
    try:
        readingtip_service.read_tip(id)
        return redirect("/")
    except AssertionError as error:
        flash_error(error)
        return redirect("/")

@app.route("/")
def userpage():
    if user_service.is_authenticated():
        tag = request.args.get("tag")
        if tag == None:
            tag = "all"
        tips = readingtip_service.get_tips(tag)
        tags = tag_service.get_tags()
        return render_template("userpage.html", tips=tips, tags=tags, filter_tag=tag)
    else:
        return render_template("login.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user_service.login(username, password):
            flash("Login successful", "success")
            return redirect("/")
        else:
            flash("Login failed", "warning")
            return redirect("/login")
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
        try:
            user_service.register(username, password)
            flash("Registration successful, you are now logged in", "success")
            return redirect("/")
        except AssertionError as error:
            flash_error(error)
            return redirect("/register")
    else:
        return render_template("register.html")

@app.route("/ping")
def ping():
    return "ping"
