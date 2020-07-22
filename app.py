from flask import Flask, redirect, url_for, request, render_template
from os import path, walk

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

Database = list()


@app.route('/')
def index():
    return render_template('homepage.html', data=Database)


@app.route("/add-post",  methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        req = request.form.to_dict(flat=False)
        print(req)
        Database.append(req)
        return redirect(request.url_root)
    return render_template("addpost.html")


if __name__ == '__main__':
    app.run()
