from app import app
from services.readingtip_service import readingtip_service
from flask import redirect, render_template, request, flash

@app.route("/newtip", methods=["POST"])
def newtip():
    title = request.form["title"]
    if readingtip_service.contains_title(title):
        flash(f"Tips already contains tip with title {title}")
        return redirect("/newtip")
    readingtip_service.create_tip(title, request.form["link"])
    return redirect("/")

@app.route("/newtip")
def create_tip():
    return render_template("newtip.html")

@app.route("/")
def userpage():
    tips=readingtip_service.get_tips()
    return render_template("userpage.html", tips=tips)

@app.route("/login")
def login():
    return render_template("login.html")
