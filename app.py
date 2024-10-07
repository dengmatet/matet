from cs50 import SQL
from flask import Flask, redirect, render_template, request

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///")

# Configure session


@app.route("/", methods=["GET", "POST"])
def index():
    # Validate submission
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")
    if id:
        return render_template("index.html")

    # Remember signing up
    db.execute(
        "INSERT INTO (fname, lname, email, password) VALUES(?, ?, ?, ?)",
        fname,
        lname,
        email,
        password,
    )

    # Confirm signing up
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
