from app import app
from services.readingtip_service import readingtip_service
from flask import redirect, render_template, request

@app.route("/newtip", methods=["POST"])
def newtip():
    readingtip_service.create_tip(request.form["title"], request.form["link"])
    return redirect("/") 

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/")
def index():
    tips=readingtip_service.get_tips()
    return render_template("index.html", tips=tips)