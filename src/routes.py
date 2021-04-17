from app import app
from services.readingtip_service import readingtip_service
from flask import redirect, render_template, request, flash

@app.route("/newtip", methods=["POST"])
def newtip():
    title = request.form["title"]
    if readingtip_service.contains_title(title):
        flash(f"Lukuvinkit sisältävät jo vinkin otsikolla {title}")
        return redirect("/form")
    readingtip_service.create_tip(title, request.form["link"])
    return redirect("/")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/")
def index():
    tips=readingtip_service.get_tips()
    return render_template("index.html", tips=tips)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user_service.login(username,password):
            return redirect("/")
        else:
            flash(f"Kirjautuminen epäonnistui")
            return redirect("/")

@app.route("/logout")
def logout():
    user_service.logout()
    return redirect("/")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user_service.register(username,password):
            return redirect("/")
        else:
            flash(f"Rekisteröityminen epäonnistui")
            return redirect("/")


