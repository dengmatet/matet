from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///database file/blue-chat.db")

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    # Check if the user is logged in
    if "email" or "password" in session:
        email = session["email"]
        password = session["password"]
        return f"logged in as {email}{password}"

    return render_template("index.html")


@app.route("/unsign", methods=["POST"])
def unsign():
    # forget signing
    id = request.form.get("id")
    if id:
       sign = db.execute("DELETE FROM sign WHERE id = ?", id)
    return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Validate submission
    if request.method == "POST":
        session["fname"] = request.form.get("fname")
        session["lname"] = request.form.get("lname")
        session["email"] = request.form.get("email")
        session["password"] = request.form.get("password")
    return render_template("index.html")

    # Remember signing up
    sign = db.execute("INSERT INTO sign(fname, lname, email, password) VALUES(?, ?, ?, ?)",)
    # Confirm signing up
    return redirect("/")


@app.route("/logout")
def logout():
    # Remove user session data
    session.pop("email", None)
    session.pop("password", None)
    return render_template("logged out!")


@app.route("/search")
def search():
    search = request.args.get("search")
    if search:
        shows = db.execute(
            "SELECT * FROM shows WHERE title LIKE ? LIMIT 50", "%" + search + "%"
        )
    else:
        shows = []
    return render_template("index.html", shows=shows)


if __name__ == "__main__":
    app.run(debug=True)
