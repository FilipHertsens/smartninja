from flask import Flask , render_template , url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("index.html")

@app.route("/portfolio")
def folio():
    return render_template("portfolio.html")

@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")

@app.route("/portfolio/boogle")
def boogle():
    return render_template("boogle.html")

@app.route("/portfolio/hair-salon")
def hair_salon():
    return render_template("hair.html")



if __name__ == '__main__':
    app.run(debug=True)