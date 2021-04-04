from app import app
from services.readingtip_service import readingtip_service
from flask import redirect, render_template, request

@app.route("/")
def index():
    tips = readingtip_service.get_tips()
    return render_template("index.html", tips=tips)
