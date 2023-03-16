from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

@app.route("/")
    return render_template("index.html")


@app.route("/projects")
    return render_template("projects.html")

@app.route("/education")
    return render_template("education.html")

@app.route("/about")
    return render_template("about.html")

@app.route("/resume")
    return render_template("resume.html")