from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
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