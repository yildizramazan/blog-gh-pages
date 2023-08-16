from flask import Flask, render_template
from requests import get

app = Flask(__name__)
response = get(url="https://api.npoint.io/25e0d288f42fe7019727").json()




@app.route('/')
def home():
    return render_template("index.html", posts=response)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in response:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)




if __name__ == "__main__":
    app.run(debug=True)
