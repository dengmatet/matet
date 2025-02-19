from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from helpers import random_string
import random

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///blue-chats.db")

# Reload after saving
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session
app.config["SESSION_PERMANENT"] = False

# Configure the Session to use filesystem
app.config["SESSION_TYPE"] = "filesystem"

# Initialize the session extension
Session(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", name="Text")

@app.route("/login", methods=["GET", "POST"])
def login():
    # Validate submission
    if request.method == "POST":
        session["email"] = request.form.get("email")
        session["password"] = request.form.get("password")
    return render_template("login.html" , placeholder=session.get("fname"))


@app.route("/sign", methods=["GET", "POST"])
def sign():
    # Set user session data
    if request.method == "POST":
        session["fname"] = request.form.get("fname")
        session["lname"] = request.form.get("lname")
        session["email"] = request.form.get("email")
        session["password"] = request.form.get("password")
        return render_template("sign.html", first=session.get("fname"), last=session.get("lname"), email=session.get("email"))
    # Inserting to database signing up
    db.execute(
        "INSERT INTO signs (fname, lname, email, password) VALUES (?, ?, ?, ?)",
        fname,
        lname,
        email,
        password,
    )
    # Confirm signing
    return redirect("/sign")


@app.route("/logout")
def logout():
    # Remove user session data
    session.clear()
    return redirect("/")


@app.route("/unsign", methods=["POST"])
def unsign():
    # forget signing
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM signs WHERE id = ?", id)
    return redirect("/")


@app.route("/search")
def search():
    search = request.args.get("search")
    if search:
        shows = db.execute(
            "SELECT * FROM shows WHERE title LIKE ? LIMIT 50", "%" + search + "%"
        )
    else:
        shows = []
    return render_template("search.html", shows=shows)


if __name__ == "__main__":
    app.run(debug=True)
