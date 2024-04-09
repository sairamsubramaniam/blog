from flask import render_template, flash, redirect, url_for

from app import flask_app
from app.forms import LoginForm



@flask_app.route("/")
@flask_app.route("/landing_page")
def landing_page():
    return render_template("landing_page.html")


@flask_app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Creds Sent")
        return redirect( url_for("landing_page") )
    return render_template("login.html", form=form)
