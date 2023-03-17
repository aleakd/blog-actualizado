from flask import Flask, render_template, request
import requests


posts = requests.get("https://api.npoint.io/2fcf7a0eef76645c194e").json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_post=posts)


@app.route("/post/<int:index>")
def show_post(index):
     requested_post = None
     for blog_post in posts:
         if blog_post["id"] == index:
             requested_post = blog_post
     return render_template("post.html", post=requested_post)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/form-entry', methods=["POST"])
def mensaje():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>el mensaje se recibio correctamente</h1>"





if __name__ == "__main__":
    app.run(debug=True)