from flask import redirect, render_template, request, flash
from app import app
from services.readingtip_service import readingtip_service
from services.user_service import user_service
from login import (LoginService as login_service) 

@app.route("/newtip", methods=["POST"])
def newtip():
    title = request.form["title"]
    if readingtip_service.contains_title(title):
        flash(f"Tips already contains tip with title {title}")
        return redirect("/newtip")
    readingtip_service.create_tip(title, request.form["link"], login_service.current_user().get_id())
    return redirect("/")

@app.route("/newtip")
def create_tip():
    return render_template("newtip.html")

@app.route("/deletetip/<id>")
def delete_tip(id):
    user_id = login_service.current_user().get_id()
    tip_user_id = ReadingTip.query.filter_by(id=id).user_id
    if user_id == tip_user_id:
        readingtip_service.delete_tip(id)
        return redirect("/")
    else:
        flash("Delete failed")
        return redirect("/")

@app.route("/")
def userpage():
    tips=readingtip_service.get_tips()
    return render_template("userpage.html", tips=tips)

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
            flash("Registration successful, you may now log in")
            return redirect("/")
        else:
            flash("Register failed")
            return redirect("/")
    else:
        return render_template("register.html")

@app.route("/ping")
def ping():
    return "ping"
