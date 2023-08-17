from flask import Flask, render_template, request
from requests import get
import smtplib

app = Flask(__name__)
response = get(url="https://api.npoint.io/25e0d288f42fe7019727").json()
OWN_EMAIL = "YOUR EMAIL ADDRESS"
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"



@app.route('/')
def home():
    return render_template("index.html", posts=response)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        send_email(name, email, phone, message)
    return render_template('contact.html')


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in response:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)








if __name__ == "__main__":
    app.run(debug=True, port=5000)
